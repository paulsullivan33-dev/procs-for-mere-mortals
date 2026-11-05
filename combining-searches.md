# Combining searches

Outcome: when one keyword leaves too
many rows, you can combine several —
and you know which logic procs applies
when you do, because the default is
only one of four.

## Two keywords, one row

Give procs two keywords and a process
must satisfy both to survive — the
default logic is **AND**:

```text
$ procs specimen spinner
 102923 root │     98.0 0.1 00:05:17 │ python3 specimen-spinner.py
```

Of the six specimens only the spinner
is both a specimen and a spinner.
`--and` spells the same thing out;
it changes nothing (transcript
`procs-lab/transcripts/t04-search-logic.txt`
shows the two runs, identical). AND
is the narrowing tool: add words
until the table is the process you
mean — a name and its owner, a
program and its argument.

## OR: either will do

`--or` keeps a row that matches any
of the keywords:

```text
$ procs --or spinner hog
 102923 root │     96.2 0.1 00:05:17 │ python3 specimen-spinner.py
 102925 root │      0.0 3.9 00:00:00 │ python3 specimen-hog.py
```

OR is for rounding up a set — the two
browsers, the database and its
helper. Its count over a shared word
shows the union plainly:
`procs --or specimen sleeper` kept 6
rows — the six specimens, the sleeper
among them counted once, because a
row is either in the table or not.

## NAND and NOR: the world minus

The other two logics answer "everything
except":

- `--nand` keeps every process that
  does **not** match all the keywords
  together. `procs --nand specimen
  spinner` kept 33 rows — the whole
  machine minus the one process that
  is both.
- `--nor` keeps every process that
  matches **none** of the keywords.
  `procs --nor specimen spinner`
  begins with PID 1 and the system
  services — nothing specimen, nothing
  spinner, anywhere in their rows.

The difference matters: NAND excludes
the combination, NOR excludes each
word separately, so NOR's table is
always the smaller of the two. Their
household use is the negative
question — "show me everything except
the usual suspects" when hunting the
one process you did not expect.

## Which logic, when

| You want | Logic | Spelling |
| --- | --- | --- |
| rows matching all words | AND | default, or `--and` |
| rows matching any word | OR | `--or` |
| all but rows matching every word | NAND | `--nand` |
| all but rows matching any word | NOR | `--nor` |

The logic is a property of the run,
not of each keyword — you cannot mix
("this pair ANDed, that one ORed").
And the case rule and exact-number
rule from chapter 5 apply inside
every keyword exactly as before.

The default itself is a setting:
`logic = "And"` in the configuration
the settings chapter reads. Change
the file and the bare two-keyword
run changes its meaning — one more
reason chapter 12 insists you know
what your own configuration says.

Check: pick a crowded keyword on your
machine (a common program name) and
run it alone; then add a second word
with the default AND and watch the
table shrink; then the same two words
under `--or` and watch it grow past
either single search. Predict each
count before you press Enter.
