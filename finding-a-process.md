# Finding a process

Outcome: you can narrow the whole
table to the process you mean — by
name, by any word in its command
line, by its owner, or by its exact
PID — and you know why a search that
finds nothing is not an error.

## A keyword narrows the table

Any argument that is not an option is
a **keyword**, and procs keeps only
the rows that match it. The lab's six
specimens all carry the word
`specimen` in their command lines, so
(transcript
`procs-lab/transcripts/t02-finding.txt`):

```text
$ procs specimen
 PID:▲  User │ TTY  CPU MEM CPU Time │ Command
             │      [%] [%]          │
 102922 root │      0.0 0.1 00:00:00 │ python3 specimen-sleeper.py
 102923 root │     56.6 0.1 00:05:16 │ python3 specimen-spinner.py
 102924 root │      0.0 0.1 00:00:00 │ python3 specimen-server.py
 102925 root │      0.0 3.9 00:00:00 │ python3 specimen-hog.py
 102926 root │      0.0 0.0 00:00:00 │ bash specimen-family.sh
 108755 root │      0.0 0.1 00:00:02 │ python3 fixtures/specimen-burner.py
```

A more specific word selects one:

```text
$ procs sleeper
 102922 root │     0.0 0.1 00:00:00 │ python3 specimen-sleeper.py
```

Matching for text is **partial and
anywhere**: the keyword need only
appear somewhere in the text being
searched. The columns searched by
default are the **command line**, the
**user**, and the **PID** — and a
match in any one of them keeps the
row. That breadth is the finder's
strength and its weakness: a keyword
also matches words inside arguments,
file names, and even other programs'
code that happens to sit on their
command lines. The troubleshooting
chapter runs the full trap exhibit,
and the limits chapter draws the
conclusion.

## By owner

Because the user column is searched,
a user name is a keyword like any
other. The lab runs everything as one
user, which makes the demonstration
blunt but honest:

```text
$ procs root | tail -n +3 | wc -l
28
```

Twenty-eight rows matched `root` at
that moment — every process owned by
root. On your machine, your own user
name narrows the table to your
programs (plus any whose command
lines happen to contain your name —
breadth again).

## By exact PID

A keyword that is all digits is
tested against the PID column, and
number matching is **exact**:

```text
$ procs 102922
 102922 root │     0.0 0.1 00:00:00 │ python3 specimen-sleeper.py
$ procs 1029
 PID:▲ User │ TTY CPU MEM CPU Time │ Command
            │     [%] [%]          │
```

`1029` is the beginning of several
specimen PIDs and matches **none** of
them. There is no "starts with" for
numbers — a PID is a name, not a
word, and procs treats it as one.
Half a PID is not a process.

## The case rule

Text matching is **smart** about
case, the rule editors use: a keyword
typed all in lower case matches
regardless of case, while a keyword
containing a capital letter must
match exactly. The lab proved the
upper-case half with a word that
exists only in lower case (transcript
`procs-lab/transcripts/t90-trap.txt`):
`procs zanzibar` found two processes,
and `procs ZANZIBAR` found none. So
when a search comes back unexpectedly
empty, look at your own capital
letters first.

## Nothing found is not an error

A search with no matches prints the
header and nothing else, and procs
exits with code **0** — success:

```text
$ procs qqq-nothing
 PID:▲ User │ TTY CPU MEM CPU Time │ Command
            │     [%] [%]          │
exit: 0
```

That is a deliberate difference from
`grep`, which reports failure when it
finds nothing. Whether it helps or
trips you depends on context; chapter
11 takes the scripting view. Here it
is enough to know: empty table, calm
exit.

## Before you act on a PID

procs itself only looks. The usual
reason to find a PID is to act on it
— stop a runaway with `kill`, say.
The snapshot rule applies with
teeth: between your `procs` and your
`kill`, the process can exit, and
PIDs are reused, so the number can
come to name something else. Run the
search again immediately before
acting, and read the row you are
about to act on — the command, the
owner — one last time.

Check: start any long-lived program
of your own (a browser, a `sleep
600` in another terminal), then find
it three ways: by part of its name,
by its owner's name, and by its full
PID from the first search. Try its
PID with the last digit removed and
watch the table come back empty.
