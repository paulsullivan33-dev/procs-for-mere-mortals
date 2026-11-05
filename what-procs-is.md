# What procs is

Outcome: you know what question procs
answers, what it replaces, and the one
rule that governs every number it
prints.

## The question

Every running program on your machine
is a **process**: the operating system
gives each one a number (its **PID**,
process ID), an owner, some memory,
and a share of the processor. Sooner
or later you need to look at them:
something is slow, something is stuck,
something is holding a file or a port,
or you simply want to know what
started what. The traditional tool is
`ps`, and it does show all of it —
like this, from this guide's lab
machine:

```text
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.1  0.0  22088  5900 ?        Ss   06:55   0:09 /usr/lib/systemd/systemd
root           17  0.0  0.0  33972  4364 ?        Ss   06:55   0:01 /usr/lib/systemd/systemd-journald
```

Nothing there is wrong, but almost
nothing there is explained. What does
`Ss` mean? Is `%CPU` what the process
is doing now, or what it has done on
average since it started? (For `ps`,
an average over the process's whole
life — chapter 14 shows the two tools
disagreeing about the same process for
exactly this reason.) Which of the
half-dozen traditional flag bundles —
`ps aux`, `ps -ef`, `ps axjf` — gives
you the view you want, and why does
the answer change between Linux,
macOS, and the BSDs? `ps` grew by
accretion over decades, and it reads
that way.

## The replacement

**procs** is a ground-up replacement,
written in Rust by its author as "a
modern replacement for ps". One bare
command prints the whole table,
aligned, with headers in plain units:

```text
 PID:▲  User │ TTY  CPU MEM CPU Time │ Command
             │      [%] [%]          │
 1      root │        0.0 0.1 00:00:09 │ /usr/lib/systemd/systemd
 17     root │        0.0 0.1 00:00:01 │ /usr/lib/systemd/systemd-journald
```

Around that table it builds the jobs
people actually do:

- **Find** — type part of a name, an
  argument, a user, or an exact PID,
  and the table narrows to matches
  (chapters 5 and 6).
- **Choose columns** — some 76 kinds
  of fact can be columns, from TCP
  ports to start times (chapter 7).
- **Sort and tree** — order by any
  column, or draw who started whom
  (chapter 8).
- **Watch** — refresh the table every
  second, like a small, patient `top`
  (chapter 9).
- **Be scripted** — plain output in
  pipes, and JSON when a program is
  reading (chapters 10 and 11).
- **Be configured** — one file sets
  your default columns, search, and
  sort (chapter 12).

It is one program with one spelling
of its options on Linux, macOS, and
Windows — though which columns exist
differs by operating system, because
each system keeps different records;
chapter 7 and the limits chapter say
where that matters.

## The one rule

**The table is a snapshot — by the
time you read it, the system has
moved.**

procs asks the operating system for
its process records, spends a tenth
of a second measuring the rates (CPU
use is a rate: work divided by time),
prints what it found, and exits. It
is not connected to anything. A
process in your table may have exited
before your eyes reach its row; a
busy process's percentage describes
the tenth of a second procs watched,
not its character; a process that
lived for a blink between two runs is
in neither run's table. Chapter 14
demonstrates all three with the lab's
specimens, including processes built
to live for 0.15 seconds: six
snapshots caught one twice.

Hold on to the rule and most
surprises dissolve. The rest of this
guide is the machine that takes the
snapshot, part by part.

Check: if your machine already has
procs, run `procs --version` (the lab
got `procs 0.14.10`), then `procs`,
then `procs` again a moment later.
Two tables, already different — a
process started or finished, a CPU
number moved. That difference is the
rule, visible.
