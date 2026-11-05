#!/bin/sh
# render.sh - show terminal output as plain text, by stripping
# the ANSI escape sequences (colour, cursor movement, and the
# operating-system-command sequences procs uses to ask the
# terminal about itself). The transcripts also keep
# escape-visible excerpts wherever the escapes are the point.
exec sed -e 's/\x1b\[[0-9;?]*[a-zA-Z]//g' -e 's/\x1b\][^\x07\x1b]*\(\x07\|\x1b\\\)//g' -e 's/\r//g'
