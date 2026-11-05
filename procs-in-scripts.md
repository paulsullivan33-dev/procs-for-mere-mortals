# procs in scripts

Outcome: you can take procs output
into another program — as text to
cut, or as JSON to parse — knowing
its units, its exit codes, and the
one honesty rule about scripting
against a moving system.

## Text first: what a pipe gives you

Chapter 10 established the ground:
in a pipe, procs prints the plain
table, full-width, no colour, no
pager. A script consuming it faces a
table, though — aligned columns,
a two-line header, units in the
headers. For quick work the shell
idioms from the transcripts suffice:
skip the header with `tail -n +3`,
narrow with keywords before you cut,
and let `--sortd` put the row you
want on top so `head` can take it.
Anything more ambitious deserves the
JSON.

## JSON: the real interface

`--json` prints an array of objects,
one per process. The lab's server
specimen, complete (transcript
`procs-lab/transcripts/t07-json.txt`):

```text
$ procs --json --insert TcpPort 102924
[
{"PID": 102924, "User": "root", "│": "│", "TTY": "", "CPU": 0, "MEM": 83, "CPU Time": 0, "TCP": "[18089]", "│": "│", "Command": "python3 specimen-server.py"}
]
```

Read it closely — it teaches four
things no documentation sentence
would make you believe:

- **The keys are the header texts**,
  exactly as printed — `"CPU Time"`
  with its space, `"TCP"` for the
  inserted port column.
- **The separators come along.** The
  `│` column is data like any other,
  appearing (twice in the raw text;
  a JSON parser keeps one) under the
  key `"│"`. Expect it, ignore it.
- **The units change.** On paper,
  MEM for this process reads 0.1%;
  in JSON it is `83` — thousandths of
  a percent, 0.083%. CPU is in
  thousandths too, and CPU Time is in
  whole **seconds**, not the
  `00:00:00` of the table. A summary
  script ships in the lab
  (`fixtures/json-summary.py`) doing
  the division; its output over the
  specimens is the table's numbers
  restored:

```text
$ procs --json specimen | python3 fixtures/json-summary.py
python3 specimen-sleeper.py         cpu    0.0%  mem   0.1%
python3 specimen-spinner.py         cpu   94.3%  mem   0.1%
python3 specimen-hog.py             cpu    0.0%  mem   3.9%
```

- **Values are typed as they come**:
  the port is the *string* `"[18089]"`,
  an absent TTY the empty string.
  There is no schema promised beyond
  the columns you asked for — which
  is the saving grace: `--insert`
  the columns your script needs, and
  the objects carry exactly those
  keys.

## Exit codes: calm and strict

Two behaviours, both verified, pull
in opposite directions:

- **No match is success.** A keyword
  that matches nothing exits 0 with a
  header-only table (chapter 5).
  A script that treats "exit 0" as
  "found it" will act on an empty
  table. Test the rows, not the code.
- **Real errors are failures.** An
  unknown column kind in `--only`
  (chapter 7) and an unreadable
  `--load-config` file both print an
  `error:` line and exit 1. A script
  that never checks the code will
  parse an error message as data.
  Check both, for opposite reasons.

## The honesty rule for scripts

Everything chapter 1 said about
snapshots applies twice to a program
that *acts*: the PID your script
found at 09:18:21 may have exited by
09:18:22 and — PIDs being reused —
may name a different process by the
time you signal it. Discipline that
survives contact:

1. Find and act as close together as
   you can; never work from a saved
   table.
2. Before acting on a PID, ask once
   more (`procs <pid>`) and confirm
   the command is still the one you
   meant.
3. Prefer matching on more than the
   PID — owner and command together —
   so a reused number fails the check
   instead of passing it.

And a rate footnote for scripts that
sample: the per-second and CPU
figures are measured over
`--interval` (default 100 ms), so a
script that polls gets tenth-of-a-
second truths, with the wobble
chapter 14 measures. Lengthen the
interval for steadier rates, at the
cost of a slower answer.

Check: run `procs --json` on a
program of yours and find its object;
divide its CPU by 1000 and compare
with the table's figure for the same
moment. Then run your JSON through
any parser you like and confirm the
`│` key is really there.
