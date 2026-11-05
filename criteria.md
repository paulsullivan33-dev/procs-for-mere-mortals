# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 14 names what the tool
   cannot do: a table that is a snapshot of a system that has
   already moved on; a CPU percentage sampled over a tenth of
   a second that wobbles and can even read past 100; a search
   that matches any part of a command line, including other
   programs' arguments and code; a column set that differs
   between operating systems; and numbers that are only ever
   the operating system's own account of a process, never a
   promise about the next second.
8. **The one rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *the table is a snapshot;
   by the time you read it, the system has moved* — before any
   procedure depends on it, and later chapters point back to
   it where a number could be mistaken for a live fact: a CPU
   reading trusted as a process's character, a PID acted on
   after its owner has exited and the number been reused, a
   "not found" taken as proof a short-lived process never ran.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 4-CPU, 7.9 GB Ubuntu 24.04.5 sandbox.
procs **0.14.10** (revision e631556, built 2025-03-28) was the
project's official release binary for Linux
(`procs-v0.14.10-x86_64-linux.zip` from the dalance/procs
GitHub releases), run from a scratch folder rather than
installed system-wide; `ps` from procps-ng 4.0.4 was the
companion. The fixtures are the lab's own specimen processes,
in `procs-lab/fixtures/`: a sleeper, a CPU spinner, a small
server listening on 127.0.0.1 port 18089, a memory hog, a
parent script with two children, and a burner that works for
four seconds and then sleeps. Three small helpers are in
`procs-lab/`: `pty-run.py` (runs a command under a real
terminal, a pty, and answers the two questions procs asks a
terminal — a device status report and the background colour —
which the sandbox's `script(1)` terminal does not answer),
`pager-spy.sh` (a pretend pager that records being called),
and `render.sh` (strips escape codes so terminal output can
be printed). All transcripts live in `procs-lab/transcripts/`.
To keep the machine's own configuration out of the
experiments, runs were made with `HOME` pointed at an empty
folder in the lab, except where a chapter is itself about
configuration. Other tenants shared the build machine, so
transcripts occasionally include their processes; the numbers
quoted in the text are the specimens' own.

Run for real, with transcripts as evidence:

- Version lines for procs and `ps` (t00).
- The first table: the default columns over the whole
  machine, the line count of a full run, and the same
  moment seen by `ps aux` (t01).
- Finding: keyword search over all six specimens; a narrower
  keyword selecting one; exact-PID search succeeding;
  a partial PID returning an empty table; a user keyword
  matching the lab's processes (t02).
- Columns: `--insert TcpPort` showing `[18089]` for the
  server specimen and `[]` elsewhere; ElapsedTime and
  StartTime added; VmRSS showing the hog at 305.934M and
  State showing `R` for the spinner and `S` for the
  sleepers; `--use-config large`; and `--only TcpPort`
  failing with `error: kind "TcpPort" is not found in
  columns`, exit code 1 (t03).
- Search logic: two keywords narrowing to one row under the
  default AND and under `--and`; `--or` widening; `--nand`
  and `--nor` counted and sampled (t04).
- Sorting: `--sortd UsageCpu` putting the spinner first,
  `--sortd UsageMem` putting the hog first, `--sorta`
  reversing — including the cosmetic quirk that a sorted
  column is printed twice (t05).
- The tree: `--tree` with a keyword showing the specimens
  under PID 1 and the family script's two `sleep 900`
  children nested under it; the plain tree's head (t06).
- JSON: one process as a JSON object (keys are the column
  headers; CPU and MEM in thousandths of a percent; CPU
  Time in seconds; the TCP value the string `"[18089]"`),
  and a piped summary script dividing the units back (t07).
- Configuration: `--gen-config` counted (140 lines) and its
  head read; the guide's example `procs.toml` obeyed via
  `--load-config` and via `~/.procs.toml`; and the same
  columns with no searchable column set
  (`procs-no-search.toml`) returning a header-only table
  with exit code 0 (t08).
- Pipes, pager, colour: piped output containing 0 escape
  bytes; `--color always` in a pipe producing 144; a
  terminal (pty) run producing 147; the colour escapes read
  out of the header line; the pager spy, named through
  `$PAGER`, never called while the built-in pager's screen
  (continuation marks, `:` prompt) was captured on a
  12-row terminal; a full table counted through a pipe,
  where no pager engages (t09). The pager modes: `--pager
  always` paging even a two-line result (its `(END)` mark
  captured), `--pager disable` printing a full 18-line
  table straight through a 12-row terminal where the
  default held it to 11 rendered lines (t09b).
- Watch: under the pty, `procs --watch` redrawing the
  specimen table 3 times in about 3.5 seconds, its header
  line showing the 1000 ms interval and the n/p/a/d/q keys;
  Ctrl-C ending it with exit code 0 (t10, and the rendered
  session in `watch-session.txt`).
- The search trap: two processes started with the word
  `zanzibar` only as a trailing argument, both found by
  `procs zanzibar`; `procs ZANZIBAR` finding nothing under
  the smart case rule; `procs sleep` matching seven rows,
  including a shell whose command line merely contains the
  word `sleep` in its text; a nonsense keyword returning a
  header-only table with exit code 0 (t90).
- The limits exhibits: the burner asleep with procs
  reporting CPU 0.0 while `ps` reported its lifetime
  average of 32.7% for the same process, both agreeing on
  2 seconds of CPU time; the spinner read twice in a row at
  87.4 and 106.8; and six snapshots hunting 0.15-second
  mayfly processes, catching one twice (t91).
- Configuration defaults read from `--gen-config` output:
  the search defaults (numeric exact, text partial, logic
  AND, smart case), the display defaults (procs and its
  parent hidden, pipe output untruncated), and the pager
  settings — all quoted from the tool's own generated file.
  The measuring interval (`--interval`, default 100 ms) and
  the watch interval (1 second) are quoted from `--help`.

Documented only — described from the project's documentation
or `--help` text, not run, and the text does not claim
otherwise:

- The macOS and Windows builds: procs is one program on all
  three systems, but which column kinds exist differs by
  operating system. Only the Linux build (76 column kinds
  via `procs --list`) was run; the text says to check
  `--list` on your own system rather than trusting this
  guide's catalogue.
- The package installation routes (the project's packages
  and `cargo install procs`): the lab ran the release
  binary. Ubuntu 24.04's apt archive was checked and has no
  `procs` package (only an unrelated Python library,
  `python3-procs`).
- The headless-browser columns and other kinds the sandbox
  could not exercise, and the Docker columns (no Docker
  daemon in the sandbox).
- Interactive watch-mode and pager key presses beyond the
  ones captured: the transcripts drive the terminal stand-in
  with single keys (`q`, Ctrl-C); the rest are named from
  the on-screen header and the help text.
- The XDG configuration path
  (`~/.config/procs/config.toml`) named in the project's
  documentation; the lab verified `~/.procs.toml` and
  `--load-config` and the text leans on those.
- The neighbouring tools in chapter 13 (top, htop, btop)
  are characterised from their documented behaviour, not
  run side by side or benchmarked; `ps` itself was run, and
  its output is quoted in chapters 1 and 14.

Fixtures are this guide's own and deliberately generic: six
small specimen programs started by the lab itself — a
sleeper, a spinner, a socket server, a memory hog, a parent
with two children, and a burner — plus two argument-carrying
sleepers and a mayfly respawner for the limits exhibits. No
example is modelled on any real person, network, service or
organisation.
