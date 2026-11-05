# Sorting and the tree

Outcome: you can put the greediest
process at the top of the table, and
you can draw the family tree that
shows who started whom.

## Sorting by any column

`--sortd <kind>` sorts descending —
biggest first — and `--sorta` sorts
ascending. The "who is eating the
machine" question is one command
(transcript
`procs-lab/transcripts/t05-sorting.txt`):

```text
$ procs --sortd UsageCpu | head -7
 PID    User │ TTY   CPU:▼ MEM CPU Time  CPU │ Command
 102923 root │        98.0 0.1 00:05:18 98.0 │ python3 specimen-spinner.py
 67     root │        29.4 4.6 00:10:30 29.4 │ /opt/hatch/bin/hatch daemon --runtime-cell-leader=2233
 748    root │         9.8 0.2 00:01:11  9.8 │ /opt/hatch/bin/hatch-execd --runtime-cell-leader=2233
 1      root │         0.0 0.1 00:00:09  0.0 │ /usr/lib/systemd/systemd
 108938 root │         0.0 0.0 00:00:00  0.0 │ head -7
```

The spinner, at 98.0, leads the
machine. Even `head -7` itself made
the table — procs hides its own row,
not its neighbours'. Two details to
read in that header. The sort arrow now sits on
CPU and points down — `CPU:▼`, where
chapter 4 had `PID:▲` — so the table
always confesses its order. And the
CPU column appears **twice**: once in
its usual place, once again before
Command. That duplication is a
cosmetic quirk the lab observed in
0.14.10 whenever the sort column is
already in the table (sorting the
specimens by `UsageMem` does the same
with MEM, the hog correctly first at
3.9). The values agree; only the
layout doubles. Sort by a column not
in the table and it appears once —
as the sort.

Sorting applies to the filtered
table, which is the useful order of
operations: `procs --sortd UsageMem
specimen` ranked just the six
specimens (hog, then a four-way tie
at 0.1, then the family script at
0.0). Search first, sort second, and
small questions stay small.

Ties are worth a word: four specimens
share MEM 0.1, and their order within
the tie is nothing to read meaning
into. A snapshot does not rank what
it cannot separate.

## The tree

`--tree` redraws the table as a
family tree. A first column of
line-drawing characters (the
`TreeSlot` kind) shows each process's
place, and with a keyword the tree
keeps the matches **plus their
parents and their children** — both
are defaults in the configuration:

```text
$ procs --tree specimen
 ├┬────── 1      root │      0.0 0.1 00:00:09 │ /usr/lib/systemd/systemd
 │├────── 102922 root │      0.0 0.1 00:00:00 │ python3 specimen-sleeper.py
 │├────── 102923 root │     97.3 0.1 00:05:18 │ python3 specimen-spinner.py
 │├────── 102926 root │      0.0 0.0 00:00:00 │ bash specimen-family.sh
 │ ├───── 102928 root │      0.0 0.0 00:00:00 │ sleep 900
 │ └───── 102929 root │      0.0 0.0 00:00:00 │ sleep 900
```

Read it as genealogy. The five
specimens started detached have been
adopted by PID 1 — when a process's
parent exits, the system reparents it
to the init process — so they hang
directly under `systemd`. The family
script kept its own children: the
branch under 102926 deepens, and its
two `sleep 900` processes are drawn
as what they are, children that do
not carry the word `specimen` at all.
They are in the picture because the
tree shows a match's children, not
because they matched.

That is the tree's real use: not
finding a process, but understanding
the blast radius of one. The children
under a process are what else stops
when it is stopped, what else a
runaway shell has spawned, whose
work a stuck parent is holding up.
The full `procs --tree` draws the
whole machine's genealogy the same
way (the transcript keeps its head);
on a busy system it is long, and a
keyword is the usual way in.

The tree and the snapshot rule
together explain a common sight: a
child whose parent, in the flat
table, has a different name than you
expected — it was reparented when
its real parent finished. The tree
shows the family as it stands at the
instant of the snapshot, adoptions
included.

Check: run `procs --tree` on a
program you started from your
terminal and find your shell in its
ancestry. Then `procs --sortd
UsageCpu | head` and name your
machine's greediest process out loud
— remembering it held the title for
one tenth of a second.
