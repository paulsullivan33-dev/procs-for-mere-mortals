# Installing procs

Outcome: procs is on your machine, and
`procs --version` proves it — by
whichever route fits your system.

## The route the lab used

The lab ran the project's own release
binary, so that the version in every
transcript is exactly known. From the
[procs releases page](https://github.com/dalance/procs/releases)
it took the Linux file for version
0.14.10:

```text
procs-v0.14.10-x86_64-linux.zip
```

Unzipped, it is a single file named
`procs` — no installer, no companions.
Put it somewhere on your `PATH` (a
personal `~/bin` is fine) or run it
where it lies. The check:

```text
$ procs --version
procs "0.14.10 ( rev: e631556, rustc: 1.85.1, build at: 2025/03/28 06:52:24 )"
```

(transcript
`procs-lab/transcripts/t00-version.txt`;
the same transcript keeps the
companion `ps` version, procps-ng
4.0.4.) The odd quotation marks are
procs' own — the whole version string
is quoted. The release page carries
builds for Linux, macOS, and Windows,
in the processor variants each system
needs; pick the one matching your
machine (most desktop PCs are
`x86_64`; many small boards and newer
laptops are ARM).

## The package routes

Most systems can also install procs
from a package — the project lists
packages for many Linux distributions,
Homebrew and MacPorts on macOS, Scoop
and Chocolatey on Windows, and more.
These routes are documented-only in
this guide: the lab verified the
release binary, not each wrapping, and
a package may carry an older version
than the release page. Two cautions
from the lab's own checking:

- On the lab's Ubuntu 24.04, `apt` has
  **no `procs` package** — searching
  finds only `python3-procs`, an
  unrelated Python library for reading
  `/proc`. Do not install it expecting
  this tool. On Debian and Ubuntu, use
  the release binary (or cargo, below)
  until a package exists.
- Whatever route you take, finish
  with `procs --version` and compare:
  the chapters here describe 0.14.10.

## The cargo route

procs is written in Rust, and Rust's
package tool can build it from source:

```text
cargo install procs
```

That needs a working Rust toolchain
and takes a while — it compiles, not
downloads. The version you get is the
newest the crates registry carries,
which may be newer than this guide's.
Documented-only here, on the same
terms as the packages.

## Shell completions

`procs --gen-completion-out bash`
(also `zsh`, `fish`, and others)
prints a completion script for your
shell, so column kinds and options
complete as you type; its sibling
`--gen-completion` writes the script
to a file in the current folder
instead. A nicety, not a necessity;
the project's documentation says
where each shell wants the file.

Check: `procs --version` answers with
0.14.10 (or a newer version you chose
on purpose), and bare `procs` prints
a table headed `PID:▲  User │ TTY
CPU MEM CPU Time │ Command`. If the
table appears, the install is done —
chapter 4 takes it apart.
