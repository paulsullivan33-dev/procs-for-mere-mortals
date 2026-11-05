# The neighbours

Outcome: you know which tool to reach
for among the process watchers — and
why `ps` is not going anywhere.

## ps itself

`ps` is the incumbent: present on
every Unix-like system, woven into
forty years of scripts, and not
replaced by procs in any of them —
nor should it be. Its spellings
differ by tradition (the BSD-style
`ps aux`, the Unix-style `ps -ef`),
which is exactly the friction procs
removes for a human at a terminal,
and exactly what a script that must
run everywhere cannot assume away.
Two of its habits are worth knowing
even if you never type it again:
its `%CPU` is a lifetime average,
not a current reading (chapter 14
puts the two side by side), and the
classic pipeline `ps aux | grep
name` matches the grep's own row —
the self-match that procs' hidden
self quietly avoids. Reach for `ps`
when the machine is minimal, the
script is old, or the average is
genuinely the number you want.

## top

`top` is the system's own live
monitor: a refreshing process table
under a summary of the whole machine
— load averages, CPU states, memory
and swap totals. procs' watch mode
(chapter 9) refreshes a table but
carries no such summary; it answers
"these processes, these columns",
where `top` answers "the machine,
and its loudest processes". `top`
is everywhere, needs no install, and
is the first thing to try on a
strange machine.

## htop

`htop` is the friendly interactive
monitor: coloured meters for every
core, scrolling and mouse, a tree
view, and — the decisive difference
— **actions**. From inside `htop`
you can kill, renice, trace, and
inspect a process. procs never acts;
it finds and describes. If your
question ends in doing something to
the process, `htop` finishes the job
in one place, where procs would hand
you a PID and wish you well.

## btop and the dashboards

`btop` and its kin draw the whole
machine as an instrument panel —
graphs for CPU, memory, disks,
network, and a process table among
them. That wider view, and history
over minutes rather than seconds,
belongs to the system-monitoring
layer this series covers in
*Watching Your System for Mere
Mortals*. procs is deliberately
narrower: one table, one question at
a time.

## So which, when

| The job | The tool |
| --- | --- |
| Find a process by name, argument, owner, exact PID | procs |
| "Who holds this port / started this / ate the memory", once | procs |
| The same question inside a script, as data | procs `--json` |
| Watch a chosen few processes with chosen columns | procs `--watch` |
| A live picture of the whole machine | `top` |
| Browse, then kill or renice interactively | `htop` |
| Graphs and history across the whole system | `btop`, the dashboards |
| Any machine, any age, no install | `ps`, `top` |

The pattern: the neighbours are
monitors and managers; procs is a
question-answering table. Most days
the question is what you have.

Check: the next time you reach for
`ps aux | grep`, run the procs
keyword instead and compare what
each hands you — then decide which
habit you are keeping, and for what.
