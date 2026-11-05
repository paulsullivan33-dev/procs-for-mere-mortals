# procs for Mere Mortals

Sooner or later, every computer user
asks the same question: *what is my
machine doing right now?* The classic
answer is `ps`, a tool older than most
of the machines it runs on. Its output
is a dense thicket of codes, its
options differ from system to system,
and the simple jobs — find the program
that is eating the CPU, find the one
holding that port, show me who started
what — take flags nobody remembers.
**procs** is a modern replacement for
`ps`, written in Rust: one command that
prints a clean, aligned table of
everything running, lets you find a
process by typing part of its name,
add the columns that answer your
actual question, sort, draw the family
tree, and watch the table refresh —
with the same spellings on Linux,
macOS, and Windows.

One rule governs everything it shows,
and this guide states it in chapter 1
and keeps pointing back to it: **the
table is a snapshot — by the time you
read it, the system has moved.** procs
reads the operating system's own
records, takes a tenth of a second to
measure rates like CPU use, prints
what it found, and exits. Nothing in
the table is live, some of it is
already history, and most of the ways
procs can surprise you are ways of
forgetting that.

The lab behind this guide ran the real
thing: **procs 0.14.10**, the official
release binary from the project's
GitHub releases, on a small Linux
machine, against specimen processes
the lab started for the purpose — a
sleeper that does nothing, a spinner
that burns one CPU core, a small
server holding port 18089 on
localhost, a memory hog carrying about
300 megabytes, a parent script with
two children, and a burner that worked
hard for four seconds and then went to
sleep. Against them the lab proved
that a keyword finds a process by any
part of its command line and by its
exact PID but not by half a PID; that
several keywords combine with AND, OR,
NAND and NOR; that adding columns
brings ports, memory sizes and start
times into view; that sorting and the
tree behave as described; that the CPU
percentage is a measurement taken over
a tenth of a second, wobbling from run
to run and even reading past 100 for a
one-core spinner; that short-lived
"mayfly" processes flicker in and out
of six snapshots, caught twice; that
in a pipe the output is plain text
with zero colour escapes; that on a
terminal the built-in pager takes the
table when it is taller than the
screen — while a stand-in pager set
through `$PAGER` was never called; and
that a configuration file changes the
default columns, and that a
configuration whose columns are not
marked searchable quietly makes every
search come back empty.

What the lab could not do, it did not
fake. procs asks the terminal about
itself before it paints — it sends
questions a real terminal answers — so
the lab drove it through a small
terminal stand-in of its own, and says
so where that matters. The macOS and
Windows builds, whose column sets
differ from Linux, are described from
the project's documentation and
labelled documented-only, as are the
package installs; `criteria.md` keeps
the full ledger of what was run and
what was only read.

## What this guide covers

- [**What procs is**](what-procs-is.md) —
  what `ps` shows and why it is hard to
  read, what procs puts in its place,
  and the one rule
- [**The moving parts**](the-moving-parts.md) —
  the collector, the searcher, the
  column catalogue, the sorter, the
  tree, the watch loop, and the
  terminal gate
- [**Installing procs**](installing-procs.md) —
  the release file the lab used, the
  package and cargo routes, and
  checking the install
- [**Your first table**](your-first-table.md) —
  the default columns taken one at a
  time, and what each number actually
  measures
- [**Finding a process**](finding-a-process.md) —
  searching by name, by any argument,
  by user and by exact PID, the smart
  case rule, and the empty answer that
  is not an error
- [**Combining searches**](combining-searches.md) —
  several keywords at once, and the
  AND, OR, NAND and NOR logic
- [**Choosing columns**](choosing-columns.md) —
  the 76-column catalogue, adding
  ports, sizes and times, the `large`
  built-in set, and the `--only`
  surprise
- [**Sorting and the tree**](sorting-and-the-tree.md) —
  sorting by any column, the arrow
  that marks it, and the family tree
  with its parents and children
- [**Watch mode**](watch-mode.md) —
  the self-refreshing table, its keys,
  and how its job differs from `top`
  and `htop`
- [**Pipes, pagers and colour**](pipes-pagers-and-colour.md) —
  plain pipes, the colour that
  terminals get, the built-in pager,
  and the terminal questions procs
  asks before painting
- [**procs in scripts**](procs-in-scripts.md) —
  narrow output for other programs,
  JSON with its surprising units, exit
  codes, and scripting against a
  moving system
- [**Making it yours**](making-it-yours.md) —
  the configuration file, building one
  sane personal default, and the
  searchable-columns trap
- [**The neighbours**](the-neighbours.md) —
  `ps` itself, `top`, `htop`, `btop`,
  and the system dashboards
- [**Limits**](limits.md) — the moving
  system, the sampled percentage, the
  search that matches too much, one
  machine's columns, and what a table
  can never tell you
- [**Troubleshooting**](troubleshooting.md) —
  the empty search, the missing
  column, the frozen start, the wide
  table, and the ignored config
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Killing, pausing, or reprioritising
processes — procs is a reader, like
`ps`; it finds the PID and leaves the
acting to you and to tools such as
`kill` and `renice`, and chapter 5
says plainly what to check before you
act on a number from a snapshot.
System-wide monitoring over time —
graphs, history, alerts — belongs to
the dashboards in chapter 13. And the
per-operating-system column sets
beyond Linux are pointed at in the
project's documentation rather than
catalogued here.

## How to use this guide

Read chapter 1 for the rule and
chapter 2 for the map of parts;
everything after that is a part being
opened. Chapters 4 and 5 are best done
with a terminal open — start a program
of your own and find it. Chapters 10
and 14 are the two that change how you
read every number: what a terminal
does to the output, and why the table
is already out of date. The lab's
specimens live in
`procs-lab/fixtures/`, its three
helper scripts (`pty-run.py`,
`pager-spy.sh`, `render.sh`) beside
them, and every claim's evidence in
`procs-lab/transcripts/`; its
distilled commands are
`examples/commands.txt`, its notes
`examples/lab-notes.txt`, and its two
example configurations
`examples/procs.toml` and
`examples/procs-no-search.toml`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Watching Your System for Mere Mortals](https://paulsullivan33-dev.github.io/watching-your-system-for-mere-mortals/)
- [systemd for Mere Mortals](https://paulsullivan33-dev.github.io/systemd-for-mere-mortals/)
- [Text Processing for Mere Mortals](https://paulsullivan33-dev.github.io/text-processing-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/procs-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/procs-for-mere-mortals/blob/main/LICENSE-CODE).
