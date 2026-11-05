# Watch mode

Outcome: you can leave a procs table
running and refreshing on screen,
change its sort while it runs, and
leave cleanly — and you know when
this is the right tool and when
`top` or `htop` is.

## The table, once a second

`procs --watch` does not exit. It
draws the table, waits a second,
collects again, and redraws — the
snapshot rule turned into a film,
one frame per second. A keyword
still applies, so `procs --watch
specimen` watches just the specimens.
The lab drove it under its terminal
stand-in for three and a half seconds
and then sent Ctrl-C (transcripts
`procs-lab/transcripts/t10-watch.txt`
and the rendered session,
`watch-session.txt`): the specimen
table was drawn **3 times**, and the
run ended with exit code 0.

Every frame carries a status line
the still table does not:

```text
 Interval: 1000ms, Last Updated: 2026/11/05 09:18:21 ( Next: n, Prev: p, Ascending: a, Descending: d, Quit: q or Ctrl-C )
```

The line is the whole manual for the
mode: the interval (1000 ms here),
when this frame was taken, and the
keys. **n** and **p** move the sort
to the next and previous column,
**a** and **d** set it ascending or
descending, and **q** or **Ctrl-C**
leaves. The interval itself is an
option: `--watch-interval <seconds>`
replaces the one-second default.

Watch mode is where the measuring
interval earns its keep. Each frame
measures CPU over the same tenth of a
second as a still run, so a busy
process's number flickers frame to
frame — the lab's spinner showed
78.4 in one captured frame against
98.0 in still runs. The flicker is
not a fault; it is what "right now"
actually looks like when "now" is a
tenth of a second. Chapter 14 is the
place to take that thought seriously.

## What watch mode is not

`top` has refreshed a process table
since before procs existed, and
`htop` made the genre friendly —
coloured bars, mouse, scrolling, and
keys that act on processes: kill,
renice, trace. Chapter 13 compares
them properly. The short version:
watch mode is for **watching a
question** — these processes, these
columns, this sort — with the same
spellings you would use in a still
run, especially a filtered view no
general monitor would think to show
(watch just the processes matching
one argument, say). The moment you
want to *act* from the watching
screen, or roam the whole system by
keyboard, you want `htop`'s tool, not
this one. procs never acts; it only
ever looks, in watch mode exactly as
much as out of it.

Watch mode needs a terminal — it is
a screen, not a stream — and its
frames are drawn with the same
colour and terminal behaviour as
chapter 10 describes.

Check: run `procs --watch` on your
machine, press **n** twice and watch
the sort arrow move and the status
line follow, then **q**. Run
`procs --watch` with the name of a
program you are about to use, work
in the program, and watch its CPU
row wake and settle.
