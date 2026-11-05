#!/bin/bash
# pager-spy.sh - a pretend pager. If a program hands its output
# to an external pager, and that pager is this script, the spy
# records being called in spy-called.txt and saves everything
# it is handed in spy-input.bin, in the current directory.
# The lab sets PAGER to this script and watches whether the
# files appear - the footprints are the evidence.
echo "pager-spy called with args: $*" >> spy-called.txt
cat > spy-input.bin
