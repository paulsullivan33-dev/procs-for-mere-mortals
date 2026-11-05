# Choosing columns

Outcome: you can bring the fact you
actually need — a port, a memory size,
a start time — into the table, for one
run or for good, and you know the one
way `--only` can refuse you.

## The catalogue

Everything procs can print about a
process is a **column kind**, named
with a capitalised word: `Pid`,
`UsageCpu`, `VmRss`, `TcpPort`.
`procs --list` prints them all with a
few words each — **76 kinds** in the
Linux build the lab ran. The set is
the operating system's, not procs'
invention: kinds that read Linux's
`/proc` have counterparts on macOS and
Windows only where those systems keep
the same records, so run `--list` on
your own machine before trusting any
list in this guide, this one included.

A working selection, grouped by the
question each answers:

| Question | Kinds |
| --- | --- |
| Who is it? | `Pid`, `Ppid` (parent), `User`, `Uid`, `Command`, `FileName` |
| What state is it in? | `State`, `Threads`, `Priority`, `Nice`, `Processor` (core it is on), `Wchan` (what it waits in) |
| How much processor? | `UsageCpu`, `CpuTime` |
| How much memory? | `UsageMem`, `VmRss` (resident), `VmSize` (virtual), `VmSwap`, `VmHwm` (peak resident) |
| Which network? | `TcpPort`, `UdpPort` |
| How much disk? | `ReadBytes`, `WriteBytes` (and the per-second rates in the `large` set below) |
| When? | `StartTime`, `ElapsedTime` |
| Where? | `WorkDir` (its working directory), `Env` (its environment), `Tty` |
| Plumbing | `Separator` (the `│`), `TreeSlot` (the tree's slot), `Empty` (a blank) |

## Adding columns for one run

`--insert <kind>` adds a column,
placed before the command. Here is
the question "who is holding the
port?" answered in one run
(transcript
`procs-lab/transcripts/t03-columns.txt`):

```text
$ procs --insert TcpPort specimen
 102922 root │      0.0 0.1 00:00:00      [] │ python3 specimen-sleeper.py
 102923 root │     98.0 0.1 00:05:17      [] │ python3 specimen-spinner.py
 102924 root │      0.0 0.1 00:00:00 [18089] │ python3 specimen-server.py
```

The server specimen shows `[18089]`
— the TCP port it has bound. The
others show `[]`: no TCP ports.
Finding a port's owner is this exact
manoeuvre with the port's process as
the keyword instead of the lab's.

Inserts accumulate, and each answers
in its own format:

```text
$ procs --insert TcpPort --insert ElapsedTime --insert StartTime specimen
 102924 root │      0.0 0.1 00:00:00 [18089] 7.5minutes 2026/11/05 09:10 │ python3 specimen-server.py
$ procs --insert VmRss --insert State specimen
 102923 root │     98.0 0.1 00:05:17   5.957M     R │ python3 specimen-spinner.py
 102925 root │      0.0 3.9 00:00:00 305.934M     S │ python3 specimen-hog.py
```

Three lessons in those lines.
`ElapsedTime` speaks in words —
`7.5minutes`, `12seconds` — while
`StartTime` gives the date and time
the process began. Sizes under
`VmRss` are humanised (`305.934M` for
the hog — the byte-truth behind
chapter 4's 3.9%) even though the
header still labels the column
`[bytes]`. And `State` is a single
letter with a small vocabulary, of
which the lab shows two: **R**,
running (the spinner, caught mid-
burn), and **S**, sleeping — waiting
for something, which is what nearly
every process does nearly all the
time. The full vocabulary (it adds
disk-wait, stopped, zombie and a few
more) is the kernel's, shared with
the STAT codes of `ps`.

## The large built-in set

`--use-config large` swaps in a
second factory configuration: wider,
with state, nice value, virtual and
resident sizes, TCP and UDP ports,
read and write rates in bytes per
second, and the start time:

```text
$ procs --use-config large specimen | cut -c1-165 | head -8
 PID:▲  User │ State Nice TTY  CPU MEM   VmSize    VmRSS TCP     UDP  Read Write │ CPU Time Start            │ Command
 102924 root │ S        0      0.0 0.1  16.402M   6.645M [18089] []      0     0 │ 00:00:00 2026/11/05 09:10 │ python3 specimen-server.py
```

(The lab cut the lines at 165
characters to fit this page; the run
itself was full-width.) `large` is a
good way to discover which facts
exist about your processes before you
commit to a configuration of your
own — chapter 12 builds one from a
handful of these same kinds.

## The --only surprise

`--only <kind>` promises a table of
just that column. It keeps the
promise only for columns **already in
the table**:

```text
$ procs --only TcpPort specimen
error: kind "TcpPort" is not found in columns
exit: 1
```

`TcpPort` is not among the defaults,
so there is nothing to narrow to —
and this time procs does fail, exit
code 1, with the reason printed.
`--only` narrows; `--insert` adds.
For a standing one-column view (a
ports-only table, say), the tool is
the configuration file, not a flag.

Check: on your machine, run
`procs --insert StartTime` and read
when your longest-running process
began; then `procs --use-config
large | head` and pick the three
columns you would keep. If
`--insert TcpPort` errors on your
system, `procs --list` will show you
whether your build spells it
differently — or does not have it.
