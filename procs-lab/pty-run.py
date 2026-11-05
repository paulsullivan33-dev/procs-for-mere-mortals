#!/usr/bin/env python3
"""pty-run.py - run a command under a real terminal (pty) and
print what the terminal saw, escapes and all.

The lab uses it to prove terminal-only behaviour (colour, the
pager, watch mode) in a sandbox that has no terminal of its own.

The stand-in terminal answers the two questions procs asks it:
  ESC [ 5 n   (device status report)  ->  ESC [ 0 n ("terminal OK")
  ESC ] 11;?  (background colour?)    ->  a dark background reply
A real terminal emulator answers these instantly. script(1)
does not answer at all, which leaves procs waiting forever -
that wait is itself one of the exhibits in the guide.

Usage: pty-run.py [--rows N] [--cols N] [--timeout S]
                  [--keys STR] [--keys-delay S] -- command [args...]
"""
import argparse, errno, fcntl, os, pty, select, signal, struct, sys, termios, time

ap = argparse.ArgumentParser()
ap.add_argument("--rows", type=int, default=40)
ap.add_argument("--cols", type=int, default=110)
ap.add_argument("--timeout", type=float, default=10)
ap.add_argument("--keys", default="")
ap.add_argument("--keys-delay", type=float, default=1.0)
ap.add_argument("cmd", nargs=argparse.REMAINDER)
a = ap.parse_args()
cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
if not cmd:
    sys.exit("no command given")

env = dict(os.environ, TERM="xterm-256color")
pid, fd = pty.fork()
if pid == 0:
    os.execvpe(cmd[0], cmd, env)

# parent: set the window size on the pty
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", a.rows, a.cols, 0, 0))

out = sys.stdout.buffer
buf = b""
deadline = time.time() + a.timeout
keys_at = time.time() + a.keys_delay if a.keys else None
status = None
while time.time() < deadline:
    r, _, _ = select.select([fd], [], [], 0.1)
    if fd in r:
        try:
            data = os.read(fd, 65536)
        except OSError as e:
            if e.errno == errno.EIO:
                break
            raise
        if not data:
            break
        out.write(data)
        out.flush()
        buf += data
        if b"\x1b[5n" in buf:
            os.write(fd, b"\x1b[0n")
            buf = buf.replace(b"\x1b[5n", b"", 1)
        if b"\x1b]11;?" in buf:
            os.write(fd, b"\x1b]11;rgb:0000/0000/0000\x1b\\")
            buf = buf.replace(b"\x1b]11;?", b"", 1)
    if keys_at and time.time() >= keys_at:
        os.write(fd, a.keys.encode())
        keys_at = None
    wpid, sts = os.waitpid(pid, os.WNOHANG)
    if wpid == pid:
        status = sts
        break
else:
    os.kill(pid, signal.SIGKILL)
    _, status = os.waitpid(pid, 0)
    print("\n[pty-run: timed out, killed]", file=sys.stderr)
    sys.exit(124)

# drain anything left
try:
    while True:
        r, _, _ = select.select([fd], [], [], 0.2)
        if fd not in r:
            break
        data = os.read(fd, 65536)
        if not data:
            break
        out.write(data)
except OSError:
    pass
sys.exit(os.waitstatus_to_exitcode(status) if status is not None else 0)
