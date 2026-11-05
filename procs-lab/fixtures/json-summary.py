import json, sys
# Reads procs --json output on stdin and prints one line per
# process: command, CPU %, memory %. In the JSON the CPU and
# MEM values arrive in thousandths of a percent (87719 means
# 87.719%), and CPU Time in whole seconds - so divide by 1000.
for r in json.load(sys.stdin):
    print(f"{r['Command']:<35} cpu {r['CPU']/1000:6.1f}%  mem {r['MEM']/1000:5.1f}%")
