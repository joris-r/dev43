#!/usr/bin/env python3
"""Dev43 script checks. Run from the project root.

  check.py spec [--base <rev>]    [paths] [names] [overlap] [depends]
  check.py tests [<file or dir>...] [coverage]

`--base` is the last commit before the increment (default: HEAD); it
sets which operations count as changed. `tests` reads the given files,
or by default every tracked or untracked file outside docs/ and
docs_future/ whose path contains "test".

Prints one line per finding and exits 1 if there is any.
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

DOCS = Path("docs")
FUTURE = Path("docs_future")

H1 = re.compile(r"^#\s")
H2 = re.compile(r"^##\s+(.*?)\s*$")
TAG = re.compile(r"^\s*(?:[-*]\s+)?\[([a-z0-9][a-z0-9-]*)\]")
ITEM = re.compile(r"^\s*[-*]\s")
CITE = re.compile(r"(?<![\w/.:~<>%-])/[a-z0-9][a-z0-9-]*(?:/[a-z0-9][a-z0-9-]*)*")
EXTENDS = re.compile(r"^Extends\s+(/\S+?)\.?\s*$")
DEPENDS = re.compile(r"^Depends on:\s*(.*)$")
INLINE_CODE = re.compile(r"`[^`]*`")

findings = []


def report(check, origin, message):
    line = f"[{check}] {origin[0]}:{origin[1]}: {message}"
    if line not in findings:
        findings.append(line)


def slug(text):
    """Lowercase ASCII: accents removed, spaces to hyphens, rest dropped."""
    text = text.lower().replace("œ", "oe").replace("æ", "ae")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9 -]", "", text)
    return re.sub(r" +", "-", text.strip())


def strip_code(text, open_span):
    """Text outside inline code; a span may wrap onto the next line."""
    out, parts = [], text.split("`")
    for k, part in enumerate(parts):
        if not open_span:
            out.append(part)
        if k < len(parts) - 1:
            open_span = not open_span
    return " ".join(out), open_span


def is_fence(text):
    return text.lstrip().startswith("```")


# A tree maps a path relative to its root ("tasks/operations.md") to its
# lines, each a (text, origin) pair, origin being (file, line number).

def read_lines(path):
    text = path.read_text(encoding="utf-8")
    return [(t, (path.as_posix(), n)) for n, t in enumerate(text.splitlines(), 1)]


def md_files(root):
    for p in sorted(root.rglob("*.md")):
        if "design" not in p.relative_to(root).parts[:-1]:
            yield p


def load_tree(root):
    if not root.is_dir():
        return {}
    return {p.relative_to(root).as_posix(): read_lines(p) for p in md_files(root)}


def tree_from_git(rev):
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", rev, "--", str(DOCS)],
                         capture_output=True, text=True)
    tree = {}
    if out.returncode:
        return tree
    for name in out.stdout.splitlines():
        rel = Path(name).relative_to(DOCS)
        if not name.endswith(".md") or "design" in rel.parts[:-1]:
            continue
        show = subprocess.run(["git", "show", f"{rev}:./{name}"], capture_output=True, text=True)
        if show.returncode == 0:
            tree[rel.as_posix()] = [(t, (name, n)) for n, t in
                                    enumerate(show.stdout.splitlines(), 1)]
    return tree


# Applying a future version to docs/.

def section_end(lines, pos):
    for k in range(pos + 1, len(lines)):
        if H2.match(lines[k][0]):
            return k
    return len(lines)


def find(lines, pos, pred):
    for k in range(pos + 1, section_end(lines, pos)):
        if pred(lines[k][0]):
            return k
    return None


def apply_feature(base, feature_dir):
    tree = {k: list(v) for k, v in base.items()}
    for path in md_files(feature_dir):
        rel = path.relative_to(feature_dir).as_posix()
        if rel == "BACKLOG.md":
            continue
        cur = tree.setdefault(rel, [])
        pos = -1
        for raw, origin in read_lines(path):
            text = raw.rstrip()
            if text.startswith("×"):
                content = text[1:].strip()
                k = find(cur, pos, lambda t: t.strip() == content)
                if k is None:
                    report("overlap", origin, "removed line not found in docs/")
                    continue
                del cur[k]
                pos = k - 1
            elif text.endswith("…"):
                prefix = text[:-1].strip()
                k = find(cur, pos, lambda t: t.strip().startswith(prefix))
                if k is None:
                    report("overlap", origin, "context line not found in docs/")
                    continue
                pos = k
            elif H1.match(text) and any(t.strip() == text for t, _ in cur):
                pos = next(k for k, (t, _) in enumerate(cur) if t.strip() == text)
            elif H2.match(text):
                k = next((k for k, (t, _) in enumerate(cur) if t.rstrip() == text), None)
                if k is None:
                    k = section_end(cur, pos)
                    cur.insert(k, (raw, origin))
                pos = k
            else:
                cur.insert(pos + 1, (raw, origin))
                pos += 1
    return tree


# Indexing a tree.

class Index:
    def __init__(self, tree):
        self.tree = tree
        self.targets = set()
        self.domains = set()
        self.sections = []   # (domain, file stem, name, slug, origin)
        self.tags = []       # (path, origin, statement)
        self.cites = []      # (path, origin, file rel)
        self.depends = {}    # domain -> [(path, origin)]
        self.extends = []    # (domain, extended path, own path, origin)
        for rel, lines in tree.items():
            parts = rel.split("/")
            domain = "/".join(parts[:-1])
            if domain:
                for i in range(1, len(parts)):
                    self.domains.add("/".join(parts[:i]))
            self.parse(rel, domain, parts[-1][:-3].lower(), lines)
        for d in self.domains:
            self.targets.add("/" + d)

    def parse(self, rel, domain, stem, lines):
        base = "/" + (domain + "/" if domain else "") + stem
        self.targets.add(base)
        section, sec_path, seen, code, span = None, base, {}, False, False
        for i, (text, origin) in enumerate(lines):
            if is_fence(text):
                code, span = not code, False
                continue
            if code:
                continue
            if not text.strip() or text.startswith("#"):
                span = False
            m = H2.match(text)
            if m:
                section, sec_path, seen = m.group(1), base + "/" + slug(m.group(1)), {}
                self.targets.add(sec_path)
                self.sections.append((domain, stem, section, slug(section), origin))
                continue
            plain, span = strip_code(text, span)
            m = DEPENDS.match(text)
            if m and stem == "readme":
                self.depends[domain] = [(c, origin) for c in CITE.findall(INLINE_CODE.sub("", m.group(1)))]
                continue
            m = EXTENDS.match(text)
            if m and stem == "operations" and section:
                self.extends.append((domain, m.group(1), sec_path, origin))
            for c in CITE.findall(plain):
                self.cites.append((c, origin, rel))
            m = TAG.match(text)
            if m:
                tag = m.group(1)
                if tag in seen:
                    report("paths", origin, f"tag [{tag}] already used in this section, line {seen[tag][1]}")
                    continue
                seen[tag] = origin
                path = sec_path + "/" + tag
                self.targets.add(path)
                self.tags.append((path, origin, self.statement(lines, i)))

    @staticmethod
    def statement(lines, i):
        out = [lines[i][0]]
        for text, _ in lines[i + 1:]:
            if not text.strip() or ITEM.match(text) or text.startswith("#"):
                break
            out.append(text)
        return " ".join(t.strip() for t in out)

    def domain_of(self, path):
        segs = path.strip("/").split("/")
        for n in range(len(segs), 0, -1):
            d = "/".join(segs[:n])
            if d in self.domains:
                return d
        return ""

    def deps(self, domain):
        return [self.domain_of(c) or c.strip("/") for c, _ in self.depends.get(domain, [])]


# spec

def check_paths(index, origins_from=None):
    for path, origin, rel in index.cites:
        if origins_from and not origin[0].startswith(origins_from):
            continue
        if path not in index.targets:
            report("paths", origin, f"{path} does not resolve")


def check_no_future_in_docs():
    for rel, lines in load_tree(DOCS).items():
        for text, origin in lines:
            if "docs_future" in text:
                report("paths", origin, "docs/ cites docs_future/")


def check_names(index, origins_from=None):
    by_slug = {}
    for domain, stem, name, s, origin in index.sections:
        by_slug.setdefault(s, {}).setdefault(name, origin)
    for s, names in by_slug.items():
        if len(names) > 1:
            for name, origin in names.items():
                if origins_from and not origin[0].startswith(origins_from):
                    continue
                others = ", ".join(f'"{n}"' for n in names if n != name)
                report("names", origin, f'section "{name}" also named {others}')


def check_depends(index, origins_from=None):
    def mine(origin):
        return not origins_from or origin[0].startswith(origins_from)

    for d, deps in index.depends.items():
        for c, origin in deps:
            if c.strip("/") not in index.domains and mine(origin):
                report("depends", origin, f"{c} is not a domain")
    for path, origin, rel in index.cites:
        own = "/".join(rel.split("/")[:-1])
        target = index.domain_of(path)
        if target and target != own and target not in index.deps(own) and mine(origin):
            report("depends", origin, f"{path}: /{own or '(top level)'} does not declare /{target}")
    state = {}

    def visit(d, trail):
        state[d] = 1
        for e in index.deps(d):
            if state.get(e) == 1:
                cycle = " -> ".join("/" + x for x in trail[trail.index(e):] + [e]) if e in trail else "/" + e
                report("depends", index.depends[d][0][1], f"dependency cycle: {cycle}")
            elif e in index.domains and not state.get(e):
                visit(e, trail + [e])
        state[d] = 2

    for d in sorted(index.domains):
        if not state.get(d):
            visit(d, [d])
    for domain, path, own, origin in index.extends:
        target = index.domain_of(path)
        if not mine(origin):
            continue
        ok = (path in index.targets and target and target in index.deps(domain)
              and path.startswith(f"/{target}/operations/"))
        if not ok:
            report("depends", origin, f"Extends {path}: not an operation of a declared domain")


def dependents(index, domain):
    out = set()
    for d in index.domains:
        stack, seen = [d], set()
        while stack:
            x = stack.pop()
            for e in index.deps(x):
                if e not in seen:
                    seen.add(e)
                    stack.append(e)
        if (domain in seen or not domain) and d != domain:
            out.add("/" + d)
    return sorted(out)


def operations(tree):
    out = {}
    for rel, lines in tree.items():
        if rel.split("/")[-1] != "operations.md":
            continue
        domain = "/".join(rel.split("/")[:-1])
        base = "/" + (domain + "/" if domain else "") + "operations"
        name, body = None, []
        for text, _ in lines + [("## ", None)]:
            m = H2.match(text) if text != "## " else True
            if m:
                if name:
                    out[base + "/" + slug(name)] = (domain, "\n".join(body).strip())
                name, body = (m.group(1) if m is not True else None), []
            elif name:
                body.append(text)
    return out


def list_changes(label, index, before, after):
    lines = []
    for path, (domain, body) in sorted(after.items()):
        if before.get(path, (None, None))[1] == body:
            continue
        deps = dependents(index, domain) if domain else ["every domain"]
        ext = sorted(own for _, p, own, _ in index.extends if p == path)
        lines.append(f"  {path}: dependents {', '.join(deps) or 'none'}; "
                     f"extensions {', '.join(ext) or 'none'}")
    if lines:
        print(f"Changed operations, {label}:")
        print("\n".join(lines))


def cmd_spec(args):
    docs = load_tree(DOCS)
    index = Index(docs)
    check_paths(index)
    check_no_future_in_docs()
    check_names(index)
    check_depends(index)
    base_ops = operations(tree_from_git(args.base))
    list_changes(f"docs/ since {args.base}", index, base_ops, operations(docs))
    if FUTURE.is_dir():
        for feature in sorted(p for p in FUTURE.iterdir() if p.is_dir()):
            applied = apply_feature(docs, feature)
            prefix = feature.as_posix() + "/"
            findex = Index(applied)
            backlog = feature / "BACKLOG.md"
            if backlog.exists():
                span = False
                for text, origin in read_lines(backlog):
                    if not text.strip() or text.startswith("#"):
                        span = False
                    plain, span = strip_code(text, span)
                    for c in CITE.findall(plain):
                        findex.cites.append((c, origin, "BACKLOG.md"))
            check_paths(findex, prefix)
            check_names(findex, prefix)
            check_depends(findex, prefix)
            list_changes(f"feature {feature.name}", findex, operations(docs), operations(applied))


# tests

def default_test_files():
    out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"],
                         capture_output=True, text=True).stdout.splitlines()
    return [Path(p) for p in out
            if not p.startswith(("docs/", "docs_future/")) and "test" in p.lower()]


def expand(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from (f for f in sorted(p.rglob("*")) if f.is_file())
        elif p.is_file():
            yield p


def cmd_tests(args):
    index = Index(load_tree(DOCS))
    known = set(index.domains) | {t.strip("/").split("/")[0] for t in index.targets}
    cited = set()
    for f in expand(args.files) if args.files else default_test_files():
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for n, text in enumerate(lines, 1):
            for c in CITE.findall(text):
                if c.strip("/").split("/")[0] not in known:
                    continue
                if c in index.targets:
                    cited.add(c)
                else:
                    report("coverage", (f.as_posix(), n), f"{c} does not resolve")
    for path, origin, stmt in index.tags:
        if path not in cited and "(not testable)" not in stmt:
            report("coverage", origin, f"{path} has no test")
    for domain, stem, name, s, origin in index.sections:
        path = "/" + (domain + "/" if domain else "") + stem + "/" + s
        if stem == "scenarios" and path not in cited:
            report("coverage", origin, f"scenario {path} has no test")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    spec = sub.add_parser("spec")
    spec.add_argument("--base", default="HEAD")
    tests = sub.add_parser("tests")
    tests.add_argument("files", nargs="*")
    args = parser.parse_args()
    {"spec": cmd_spec, "tests": cmd_tests}[args.cmd](args)
    for f in findings:
        print(f)
    print(f"{len(findings)} finding(s)." if findings else "All checks pass.")
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
