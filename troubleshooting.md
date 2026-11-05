# Troubleshooting

Outcome: the surprises every procs
user meets once, each with the check
that names it. Every one of these
happened in this guide's lab, and the
fix is a chapter that already exists
— this page is the index of mishaps.

## "procs found a process that isn't the program I named"

Almost certainly, it is the **trap**:
substring search over whole command
lines. The lab built the exhibit on
purpose (transcript
`procs-lab/transcripts/t90-trap.txt`).
Two sleepers were started carrying a
nonsense word, `zanzibar`, purely as
a trailing argument — it is not
their name, not their program, just
text on their command lines:

```text
$ python3 -c "import time; time.sleep(300)" zanzibar &
$ python3 -c "import time; time.sleep(300)" aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa zanzibar &
$ procs zanzibar
 109092 root │     0.0 0.1 00:00:00 │ python3 -c import time; time.sleep(300) zanzibar
 109093 root │     0.0 0.1 00:00:00 │ python3 -c import time; time.sleep(300) aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa zanzibar
```

Both are "found" — correctly, by the
rules of chapter 5: the word appears
in the text being searched. The same
run's `procs sleep` returned seven
rows: the lab's sleeper and two
`sleep 900` children (genuine), the
two zanzibar sleepers (the words
`time.sleep` are in their code), one
transient `sleep 3`, and a shell
whose long command line happens to
contain the words `&& sleep 1` in its
script text. Check: read the whole
command line of any surprising row
before believing the match. Fix: add
a second keyword (chapter 6) until
the pretenders fall away, and
remember that a match means "the
word is in the row", never "the row
is the program".

## "My search finds nothing"

Work the four causes in order; all
four are silent and all exit 0.

- **Your capitals.** The smart case
  rule (chapter 5): a keyword with a
  capital letter must match exactly.
  In the trap run, `procs ZANZIBAR`
  found nothing while `procs
  zanzibar` found two. Check: retype
  the keyword in lower case.
- **Half a PID.** Number matching is
  exact (chapter 5): `procs 1029`
  matched none of the 1029xx
  processes. Check: use the full PID
  from a name search first.
- **An unsearchable configuration.**
  If bare `procs` looks right but no
  keyword ever matches, your config's
  columns may carry no search
  switches — chapter 12 built that
  failure deliberately. Check: run
  once with `--load-config` pointed
  at nothing you own (or move
  `~/.procs.toml` aside) and search
  again.
- **It already left.** Short-lived
  processes fall between snapshots
  (chapter 14's mayflies). "Not
  found" is not "never ran".

## "procs hangs — or prints nothing — at start"

Under an unusual terminal, procs can
wait forever for an answer to the
questions it asks before painting
(chapter 10): the lab's `script(1)`
terminal never answers, and procs
under it produced nothing at all.
Check: does it work in your ordinary
terminal emulator? Then the terminal
was the story. Fix: `--theme dark`
or `--theme light` removes the
background question; a stand-in
terminal must answer the status
question, as the lab's `pty-run.py`
does.

## "--only says my column is not found"

The error is exact:
`error: kind "TcpPort" is not found
in columns`, exit 1 (chapter 7).
`--only` narrows the columns already
active; it cannot introduce one.
Fix: `--insert` the kind, or put it
in your configuration. If `--insert`
itself errors, compare your spelling
against `procs --list` — kinds are
case-sensitive words, and a kind
your operating system's build lacks
will not be there at all.

## "The CPU number changes every run — once it read over 100"

Not a fault: it is a measurement
over a tenth of a second, on a scale
of whole cores (chapters 4 and 14).
The lab's one-core spinner read 87.4
and then 106.8 back to back. Check:
watch the same process several times
and read the range, not a point. If
you need steadier figures, lengthen
`--interval` — and remember `ps`'s
percentage would be answering a
different question entirely.

## "Long lines are cut off"

On a terminal, procs trims the table
to the window's width
(`cut_to_terminal` in the
configuration). In a pipe it never
trims. Fix for the full text: pipe
the run — `procs foo | cat`, or into
a file — or narrow the table with
fewer columns (chapter 12) until it
fits the window honestly.

## "My pager settings are ignored"

They would be: the pager is
procs' own built-in one, and the lab's
pager spy, named through `$PAGER`,
was never called while paging plainly
happened (chapter 10). Fix in the
right vocabulary: `--pager disable`
never pages, `--pager always` pages
even a two-line result. There is no
setting that substitutes an external
pager on this build.

## "My configuration is ignored"

A configuration procs cannot read is
an error, not a shrug — a missing
`--load-config` file exits 1 with the
reason printed. So a silently ignored
config is almost always a config in
the wrong place. Check the spelling
and place: `~/.procs.toml`. Prove the
file itself with `--load-config
<your file>` on a search: if the
columns change there, the file is
fine and the home copy is not where
procs looks; if they do not, edit
the file you just proved.

Check: keep this page's habit — for
any surprise, first ask *which part*
(chapter 2) owns the behaviour, then
run that part's one-command check.
Most procs mysteries are one of the
eight above wearing a new coat.
