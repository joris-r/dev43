# UI

## General

One command, `todo`, with a subcommand per operation.

- [errors] Errors go to stderr with exit code 1; otherwise exit code 0.
- [usage] Without a subcommand, or with an unknown one, `todo` prints
  its usage and exits with code 1.

## Add

`todo add <text>` runs /operations/add. The text is the rest of the
line, words joined by spaces.

```
$ todo add buy milk
Added 1: buy milk
```

## List

`todo list` runs /operations/list. One line per task: its number, a
done mark, then its text.

```
$ todo list
1  [ ] buy milk
2  [x] call Ann
```

- [empty] Empty list: one line saying so.

```
$ todo list
Nothing to do.
```

## Done

`todo done <number>` runs /operations/done.

```
$ todo done 2
Done 2: call Ann
$ todo done 7
No task 7.
```

## Remove

`todo rm <number>` runs /operations/remove.

```
$ todo rm 1
Removed 1: buy milk
```
