import time
# Specimen: holds about 300 MB of memory, then sleeps.
buf = bytearray(300 * 1024 * 1024)
for i in range(0, len(buf), 4096):
    buf[i] = 1
time.sleep(900)
