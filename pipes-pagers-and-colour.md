# Pipes, pagers and colour

Outcome: you can predict, before you
press Enter, whether a given procs
command will produce colour, a pager,
or a plain full-width table — and you
know the one oddity that can make it
seem to hang.

## In a pipe, procs is plain

The proof is a count (transcript
`procs-lab/transcripts/t09-pipes-pagers-colour.txt`).
Colour, for a terminal, is carried by
**escape bytes** — control characters
that tell the terminal to change
colour. Count them in a pipe:

```text
$ procs specimen | tr -cd '\033' | wc -c
0
```

Zero. Piped, procs prints plain text:
no colour, no pager, and — the
configuration's `cut_to_pipe = false`
default — **no trimming**: command
lines run to their full length, which
is why the transcripts in this guide,
all captured through pipes or files,
show commands uncut. This is what
makes procs safe in scripts and
pipelines (chapter 11): the program
downstream gets text it can parse,
never the decorated picture.

Two switches govern the terminal
behaviour, each with the values
*auto*, *always*, and *disable*:

- `--color` — when to emit the colour
  escapes. *auto* (default) colours
  only for a terminal. `--color
  always` forces them into a pipe —
  the same count then reads **144** —
  and the escapes, read out loud with
  `sed -n l`, show the header wrapped
  in `38;5;15`, a numbered colour from
  the 256-colour palette. That is how
  this guide captured colour it could
  print.
- `--pager` — when the built-in
  pager, below, takes the table.

## On a terminal, colour and questions

Under the lab's terminal stand-in, the
same specimen table carried **147**
escape bytes — colour, plus something
a pipe never sees: before painting,
procs **asks the terminal questions**.
It sends a device status report
request ("are you there?") and, with
the theme on its *auto* default, an
operating-system query for the
terminal's background colour, so it
can choose a dark-on-light or
light-on-dark theme. A real terminal
emulator answers instantly and you
will never notice.

The lab noticed, because its first
stand-in terminal (`script(1)`) does
not answer questions. procs, waiting
for a reply, produced **no output at
all** — not an error, just silence,
until the lab stopped it. The lab's
second stand-in (`pty-run.py`, which
answers) made everything behave.
Two things to keep: if procs ever
seems to hang at start-up under an
exotic terminal, this is the likely
story; and `--theme dark` or
`--theme light` settles the
background question without asking,
which is also the fix for a theme
that guesses wrong.

## The pager is built in

When the table is taller than the
terminal, procs does not print it and
let it scroll: it hands it to a
**built-in pager** — its own, inside
the program. The lab proved whose
pager it is by substitution. It set
`$PAGER` to a **pager spy** (a script
that records being called), then ran
procs under a 12-row terminal:

```text
$ cat spy-called.txt
cat: spy-called.txt: No such file or directory
```

The spy was never called — yet the
table plainly paged: the rendered
capture shows rows ending in `>`
continuation marks and the pager's
`:` prompt at the bottom, and `q`
left it. There is no external pager
in the loop to configure; `$PAGER`
and friends are simply not consulted
on this build. (The generated
configuration carries a `use_builtin`
pager setting; whatever it may switch
on other builds, in every lab run the
internal pager did the work.)

Behaviour, all of it run
(transcript t09b keeps the modes):

- Table taller than the screen: the
  pager takes it. On the 12-row
  terminal the full table rendered as
  11 lines before `q` — one screen,
  the rest held back.
- Table fits: it prints straight,
  pager unseen.
- `--pager always`: the pager takes
  even a two-line result — the
  capture ends with the pager's
  `(END)` mark.
- `--pager disable`: no pager ever;
  the same 12-row terminal received
  the full 18-line table straight
  through.
- In a pipe: no pager under any
  setting that matters — chapter 11's
  territory.

Check: in your terminal, run
`procs` and watch for the pager if
your table is long (`q` to leave);
run `procs | wc -l` and see the full
count a pipe gets; and run
`procs --pager always` on a search
with one result to meet the `(END)`
mark. Three behaviours, each
predictable from where the output is
going.
