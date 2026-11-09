# UI

## List

× `todo list` runs /operations/list. One line per task: its number, a
× done mark, then its text.
`todo list [<tag>]` runs /operations/list. One line per task: its
number, a done mark, its text, then its tags, each after a `#`.

- [order] Tags in alphabetical order.

```
$ todo list
1  [ ] buy milk  #shop #urgent
2  [x] call Ann  #work
$ todo list shop
1  [ ] buy milk  #shop #urgent
```

- [nomatch] No task has the tag: one line saying so.

```
$ todo list garden
No task tagged garden.
```

## Tag

`todo tag <number> <tag>` runs /operations/tag.

```
$ todo tag 1 Shop
Tagged 1: shop
```

## Untag

`todo untag <number> <tag>` runs /operations/untag.

```
$ todo untag 1 shop
Untagged 1: shop
```
