# Your first table

Outcome: you can read the default
table column by column and row by row,
knowing what each number measures —
and what it does not.

## The whole machine, one command

Bare `procs`, no arguments, prints
every process it can see. In the lab
the full run was 45 lines: 43
processes, plus a two-line header
(transcript
`procs-lab/transcripts/t01-first-look.txt`).
The head of it:

```text
$ procs | head -14
 PID:▲  User │ TTY    CPU MEM CPU Time │ Command
             │        [%] [%]          │
 1      root │        0.0 0.1 00:00:09 │ /usr/lib/systemd/systemd
 17     root │        0.0 0.1 00:00:01 │ /usr/lib/systemd/systemd-journald
 67     root │       29.4 4.5 00:10:28 │ /opt/hatch/bin/hatch daemon --runtime-cell-leader=2233
 748    root │       19.6 0.2 00:01:11 │ /opt/hatch/bin/hatch-execd --runtime-cell-leader=2233
 102922 root │        0.0 0.1 00:00:00 │ python3 specimen-sleeper.py
 102923 root │       98.0 0.1 00:05:13 │ python3 specimen-spinner.py
```

Your machine's cast will differ; the
columns will not. The header takes two
lines because some titles carry their
unit on the second line — `[%]` under
CPU and MEM. The `│` characters are
themselves a column kind, a separator
the configuration chooses; chapter 12
meets a table built without them.

## The columns, one at a time

**PID** — the process ID, the number
the system knows it by. The small
`▲` attached to it (`PID:▲`) is the
sort mark: the table is sorted by
this column, ascending. Sorting is
the default configuration's choice —
by column 0, ascending — and chapter
8 puts the arrow on other columns.

**User** — the account that owns the
process. The lab's sandbox runs
everything as `root`; your machine
will show your own name on your
programs and system accounts on the
rest.

**TTY** — the terminal the process is
attached to, if any. It is blank for
all six lab specimens: they were
started detached, with no terminal.
`ps` marks the same situation with a
`?`. A program you launch from your
own terminal shows that terminal
here.

**CPU [%]** — how much of one
processor the process used **during
procs' measuring interval** — the
hundred milliseconds or so between
its two looks (chapter 2). The
spinner, which does nothing but burn
one core, reads 98.0: nearly a whole
core, nearly all the time. A process
using two cores fully would read near
200 — the scale is per-core, not
per-machine. And because it is a
measurement over a sliver of time,
not a property of the process, it
wobbles: chapter 14 reads the same
spinner twice and gets 87.4 and then
106.8. `ps`'s `%CPU`, shown in
chapter 1, is a different animal
entirely: an average over the
process's whole life.

**MEM [%]** — the share of the
machine's physical memory the process
is holding. The memory hog specimen
carries about 300 megabytes of data
on a machine with about 8 gigabytes,
and reads 3.9 — the arithmetic checks
(and chapter 7 shows the same fact in
bytes: 305.934M).

**CPU Time** — the total processor
time the process has consumed since
it started, hours:minutes:seconds.
This one is a ledger, not a rate: the
spinner's 00:05:13 only ever grows,
and a process can be perfectly idle
now with a large CPU Time behind it.
Confusing the two CPU columns —
percentage the sprinter's speed,
time the distance covered — is the
most common misreading of any process
table; chapter 14 builds a specimen
whose whole job is to separate them.

**Command** — the command line the
process was started with: program and
arguments together. It is the text
your searches will match against
(chapter 5), and it can be long — in
a terminal, procs trims the table to
your window's width, while in a pipe
it prints the command in full
(chapter 10).

## One row, read aloud

The spinner's row says: process
102923, owned by root, attached to no
terminal, used 98% of one core during
the interval just measured, holds
0.1% of the memory, has consumed five
minutes and thirteen seconds of
processor in its life, and is the
Python program `specimen-spinner.py`.
Every row in every table in this
guide reads the same way.

Two absences to notice. procs does
not list **itself** — the default
configuration hides procs and the
process that launched it
(`show_self` and `show_self_parents`
in the settings chapter 12 reads) —
and it shows no total or summary
line: the table is the processes,
nothing else.

Check: run `procs` on your machine
and find a program you recognise — a
browser, an editor. Read its row
aloud in the pattern above. Then run
`procs | wc -l`: the answer minus two
(the header lines) is how many
processes your machine is carrying.
