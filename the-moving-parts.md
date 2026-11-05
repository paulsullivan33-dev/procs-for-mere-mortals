# The moving parts

Outcome: you can name the parts of
procs that each later chapter opens,
and say what each part is responsible
for — so no behaviour later is magic.

A run of procs is short: collect,
measure, filter, arrange, print. Five
parts do that work, and two more
decide how the result meets your
eyes.

## The collector

The operating system keeps the books.
On Linux, every process has a folder
in `/proc` — `/proc/102922` and
friends — holding its owner, its
command line, its memory figures, its
open network sockets, in small files
any permitted program may read. The
**collector** reads those books for
every process it can see. Two
consequences follow. procs can only
show what the system records (the
numbers are the system's own, never
procs' invention), and it can only
show the processes your account is
allowed to see.

## The measurer

Some facts are totals — memory held,
CPU seconds spent since birth. Others
are **rates**: CPU use, disk reads per
second. A rate needs two looks, one
at the start of an interval and one
at the end, with the change divided
by the time between. The **measurer**
takes that second look after an
interval of 100 milliseconds (the
`--interval` option; chapter 4 shows
what the interval does to the CPU
column). This is why procs does not
answer in quite the instant `ps`
does, and why two runs a second apart
can disagree: they measured different
tenths of a second.

## The searcher

Keywords you type are tested against
the **searchable columns** — the
columns your configuration marks as
searchable, which by default are the
PID (numbers, matched exactly), and
the user and the command line (text,
matched in part, anywhere). The
**searcher** is chapter 5 and 6's
whole subject, including its case
rule and its several-keyword logic —
and the trap that searchability lives
in the configuration, so a careless
config can switch searching off
without any error (chapter 12).

## The column catalogue

Everything procs can print about a
process is a **column kind**: 76 of
them in the Linux build the lab ran
(`procs --list` prints them all). The
default table shows seven; `--insert`
adds more for one run; the
configuration file chooses your
standing set. Rates, sizes, ports,
times, threads, owners, states — the
catalogue is chapter 7, and it is the
part that differs between operating
systems, because each system records
different facts.

## The arranger

The **arranger** orders the rows and,
on request, reshapes them: sorted by
any column (`--sortd`, `--sorta`),
with a small arrow in the header
naming the sort column; or drawn as a
**tree** (`--tree`), where indentation
and line-drawing characters show who
started whom. Chapter 8.

## The watch loop

**Watch mode** is the arranger's
table with a clock: collect, measure,
print, wait a second, repeat, with
keys to change the sort while it
runs. Chapter 9, where it is also set
against `top` and `htop`, whose job
is related but not the same.

## The terminal gate

The last part faces you. Like the
other tools in this series, procs
behaves one way to a **terminal** and
another to a **pipe**. To a terminal:
colour, a built-in pager when the
table is taller than the screen, and
tables trimmed to fit the window's
width. To a pipe: plain text, no
pager, full width, always. Before it
paints for a terminal, procs asks the
terminal two questions — are you
ready, and is your background light
or dark — and a terminal that never
answers can leave it waiting; chapter
10 proves each of these behaviours
and names the switches (`--color`,
`--theme`, `--pager`) that govern
them.

## The settings

Underneath everything sits the
**configuration**: the file
`~/.procs.toml`, if you have one,
deciding your default columns, search
behaviour, sort, colours and pager.
`procs --gen-config` prints the full
sample — 140 lines in the lab's run —
and chapter 12 builds a small,
deliberate one.

Check: run `procs --list` and count
the kinds (76 on the lab's Linux
build; your system's number may
differ). Run `procs --gen-config |
head -12` and find the first column
of the default table described —
`Pid`, with `numeric_search = true`.
Those two commands are the catalogue
and the settings introducing
themselves.
