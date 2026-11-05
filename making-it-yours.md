# Making it yours

Outcome: you have a small, deliberate
`~/.procs.toml` of your own — columns
you chose, search switches you set on
purpose — and you can prove it is
being obeyed, and diagnose the one
way it can silently break searching.

## Where the configuration lives

procs reads `~/.procs.toml` when it
exists. (The project also documents
an XDG path, `~/.config/procs/
config.toml`; the lab verified the
home file and `--load-config`, below,
and leans on those.) The full sample,
with every option and its factory
value, is one command:

```text
$ procs --gen-config | wc -l
140
$ procs --gen-config | head -12
[[columns]]
kind = "Pid"
style = "BrightYellow|Yellow"
numeric_search = true
nonnumeric_search = false
align = "Left"
```

The anatomy, in the order the file
presents it: a list of `[[columns]]`
— kind, style, the two search
switches, alignment — then `[search]`
(the defaults chapter 5 and 6 met:
numeric `"Exact"`, text `"Partial"`,
logic `"And"`, case `"Smart"`), then
`[display]` (separators, sort marks,
whether procs and its parent are
hidden, whether terminal output is
trimmed), `[sort]` (column 0,
ascending, by default), `[docker]`,
and `[pager]`. You do not need most
of it. A personal configuration is a
small file that says a few things
deliberately.

## Building one sane default

The lab's example
(`examples/procs.toml`, used in
transcript
`procs-lab/transcripts/t08-config.txt`)
keeps seven columns — PID, user, CPU,
memory, TCP ports, elapsed time,
command — chosen because they answer
the everyday questions: what, whose,
how busy, how big, holding what port,
how old, started how. Its Pid entry
carries `numeric_search = true`, and
User and Command carry
`nonnumeric_search = true`, **on
purpose** — the next section is why.

Test it before adopting it, via
`--load-config`, which uses a file
for one run:

```text
$ procs --load-config ../examples/procs.toml specimen
 PID:▲  User CPU  MEM TCP     Elapsed    Command
             [%]  [%]
 102922 root 0.0  0.1 []      7.6minutes python3 specimen-sleeper.py
 102924 root 0.0  0.1 [18089] 7.6minutes python3 specimen-server.py
 102925 root 0.0  3.9 []      7.6minutes python3 specimen-hog.py
```

Note what changed: the separators
and the TTY column are gone (the
example defines no `Separator`
column), the ports and elapsed times
are in, and the table is narrower.
Then install it — copy it to
`~/.procs.toml` — and the same bare
command obeys it:

```text
$ cp ../examples/procs.toml ~/.procs.toml
$ procs specimen
 PID:▲  User CPU  MEM TCP     Elapsed    Command
```

(`rm ~/.procs.toml` undoes it, as the
transcript does.) Command-line flags
still apply on top of your file for a
run — `--insert` adds to the active
set, `--sortd` resorts it — and
`--load-config` replaces the file
wholesale for one run, which is how
you trial a new configuration without
disturbing the old.

## The trap: a config that cannot search

Now the same columns with every
search switch left off — the lab
ships it as
`examples/procs-no-search.toml`:

```text
$ procs --load-config ../examples/procs-no-search.toml specimen
 PID:▲ User CPU MEM TCP Elapsed Command
            [%] [%]
exit: 0
```

The table prints. The columns are
right. And `specimen` — which matches
six processes under the factory
config — matches **nothing**, with a
calm exit 0 and no error anywhere.
The lesson is structural: **search
runs against the columns in the
active configuration, and only those
marked searchable**. Searching is not
a property of procs; it is a property
of your column list. Whoever builds a
configuration by naming columns and
forgetting the switches — the
switches are not in the minimal
examples floating around — switches
finding off while leaving the table
looking perfect.

The diagnosis, if it ever happens to
you: bare `procs` looks right,
keyword `procs` finds nothing, and
`procs --gen-config` next to your
file shows the difference — the
`numeric_search` and
`nonnumeric_search` lines. The fix
is those lines, set true on the
columns you search by: numbers for
the PID, text for the user and the
command, at minimum.

Check: write or copy a configuration,
prove it with `--load-config`,
install it at `~/.procs.toml`, and
run one keyword search you know
should match. Then deliberately
break a copy the no-search way and
watch a correct-looking table find
nothing — once seen, never forgotten.
