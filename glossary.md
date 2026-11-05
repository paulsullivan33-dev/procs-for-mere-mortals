# Glossary

The terms, collected in one place.
Each is defined the way this guide
uses it.

**Column kind** — One fact procs can
print about a process, named with a
capitalised word (`Pid`, `VmRss`,
`TcpPort`). 76 kinds in the Linux
build; `procs --list` shows a
system's own set.

**Command line** — The full text a
process was started with: program
plus every argument. It is the main
text keyword searches match against.

**CPU Time** — The total processor
time a process has consumed since it
started. A ledger that only grows;
not a rate.

**Elapsed time** — How long a process
has existed, from its start to the
snapshot (`7.5minutes` in procs'
words).

**Escape byte** — A control character
in terminal output that instructs
the terminal — change colour, move,
reset. Counted in chapter 10 to
prove when colour is and is not
present.

**Exact match** — The rule for
number keywords: the whole PID must
equal the keyword. Half a PID
matches nothing.

**Keyword** — A non-option argument
to procs: the word rows are tested
against when narrowing the table.

**Measuring interval** — The pause
between procs' two looks when it
computes rates such as CPU use:
100 milliseconds by default, set by
`--interval`.

**Pager** — A program for reading
long output screen by screen.
procs' pager is built into procs
itself; `--pager` chooses when it
takes the table.

**Partial match** — The rule for
text keywords: the keyword need only
appear somewhere in the text being
searched.

**PID** — Process ID: the number the
operating system knows a process by.
Unique among living processes, and
reused after a process exits.

**Process** — A running program: one
row of the table, with an owner, a
command line, memory, and a share of
the processor.

**Reparenting** — The system's
adoption of a process whose parent
has exited, usually by PID 1. Why a
tree's ancestry can differ from who
really started a process.

**Resident set** — The memory a
process actually holds in RAM, as
opposed to the larger virtual space
it has reserved. The `VmRss` column;
the basis of the MEM percentage.

**Searchable column** — A column
whose configuration entry marks it
as searched: numbers for the PID,
text for the user and command by
default. Unmarked columns are never
searched, however the table looks.

**Smart case** — The case rule for
text keywords: all lower case
matches any case; any capital letter
must match exactly.

**Snapshot** — One run's table: the
system's state gathered at one
moment, already ageing as it prints.
The guide's one rule.

**Sort mark** — The small arrow on a
column header (`▲` ascending, `▼`
descending) naming the column the
table is sorted by.

**State** — The kernel's one-letter
verdict on a process: R running, S
sleeping (waiting), and a few more,
including D (disk wait), T (stopped)
and Z (zombie — finished, awaiting
collection).

**Throughput** — Work per unit of
time: the read and write bytes per
second, and the CPU rate, that procs
derives from its measuring interval.

**Tree** — The table redrawn as
genealogy: indentation and line
characters showing each process's
parent and children.

**TTY** — The terminal a process is
attached to. Blank in the table when
the process has none, as detached
and system processes do not.
