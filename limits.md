# Limits

Outcome: you know the ways a procs
table can mislead a careful reader —
each one demonstrated in the lab, not
just asserted — and what to do
instead.

## The system has already moved

The one rule, with its evidence. The
lab built **mayflies**: processes
that live for 0.15 seconds, restarted
in a loop so that one is usually
alive. Six snapshots in a row,
counting matches (transcript
`procs-lab/transcripts/t91-limits.txt`):

```text
$ for i in 1 2 3 4 5 6; do procs mayfly | tail -n +3 | wc -l; sleep 0.4; done
0
0
1
0
0
1
```

A process that exists, doing its
short duty over and over, is absent
from most tables — each snapshot
either catches its 0.15 seconds or
does not. Lengthen the reasoning:
anything can be true of the gap
between two of your runs, and "procs
found nothing" never proves "nothing
ran". For short-lived work, the
evidence lives in logs and in the
parent's account, not in a table of
the living.

## The percentage is a sample

CPU use is measured over an interval
— 100 ms by default — and a tenth of
a second is a small sample of a
noisy world. The spinner, whose one
job is to hold a core at 100%, read
twice within moments (transcript
t91):

```text
$ procs spinner
 102923 root │     87.4 0.1 00:05:13 │ python3 specimen-spinner.py
$ procs spinner
 102923 root │    106.8 0.1 00:05:13 │ python3 specimen-spinner.py
```

87.4, then **106.8** — past the
theoretical maximum for one core.
Nothing is broken: measuring "how
much of the interval was busy"
involves counters read at slightly
different instants, on a machine
where other work competes (the
lab's burner, set to burn for four
seconds, collected only two seconds
of CPU time because the machine was
shared). Treat one reading as an
estimate with wide margins: patterns
across several readings are evidence;
a single decimal point is theatre.
For a steadier number, `--interval`
lengthens the measurement — and
slows the answer by exactly that
much.

## Now, or the average of a life

The burner, asleep after its four
seconds, in the same moment, from
the two tools (transcript t91):

```text
$ procs burner
 108755 root │     0.0 0.1 00:00:02 │ python3 fixtures/specimen-burner.py
$ ps -o pid,pcpu,time,command -p 108755
    PID %CPU     TIME     COMMAND
 108755 32.7 00:00:02 python3 fixtures/specimen-burner.py
```

procs says 0.0; `ps` says 32.7. Both
are right: procs reports the
measuring interval just past (the
burner was asleep for all of it),
while `ps`'s percentage is the
average over the process's whole
life — two CPU-seconds spread over
its first six seconds of existence.
Neither tool shows the other's
number: procs has no lifetime-average
column, `ps` has no "right now"
column. Know which question your
number answers before you quote it.
CPU Time, the ledger both agree on
(00:00:02), is the only one of the
three that never pretends to be a
rate.

## The search matches more than you meant

Finding is substring matching over
whole command lines, so it finds
processes that merely *mention* your
word — as an argument, as a file
name, as text inside a script's code.
The troubleshooting chapter's trap
exhibit is the full demonstration:
two sleepers carrying an unrelated
word as an argument are "found" by
it, and `procs sleep` returns seven
rows, most of which are not the
`sleep` program. The guard is a
second keyword (chapter 6) and
reading the row before believing it.

## One machine's columns are not every machine's

The 76 kinds in chapter 7 are what
the **Linux** build can read from
**Linux's** records. Other builds
offer other sets, and a script or a
habit that assumes `TcpPort` — or
any kind — exists everywhere will
break where it does not. `procs
--list` on the machine in front of
you is the only catalogue that
counts. The same humility applies
across versions: this guide describes
0.14.10's behaviour, quirks (the
doubled sort column among them)
included, and later versions may fix
or alter any of it.

## What a table can never tell you

- **Why.** A process at 98% may be
  doing the work you asked of it or
  spinning on a bug. The state letter
  says R; it does not say *on what*.
  Tables locate suspects; they do
  not deliver verdicts.
- **What happens next.** A quiet
  process may be finished or may be
  waiting for the hour. The snapshot
  has no future in it.
- **What you may not see.** The
  collector reads the system's
  records with your account's
  permissions; details the system
  withholds from you — another user's
  environment, say — are not in your
  table, and their absence is silent.
- **The whole machine.** procs
  counts processes. Load, memory
  pressure, disk saturation — the
  context that explains a process's
  numbers — live in the monitors of
  chapter 13.

Check: pick any row of your own
table and state, out loud, which of
its numbers is a total, which is a
sample over the last tenth of a
second, and what the row cannot tell
you at all. That discipline — totals
believed, samples suspected, futures
unclaimed — is the whole chapter.
