import time
# Specimen: burns one CPU core for about four seconds,
# then goes to sleep. Its CPU Time keeps the four seconds
# forever; its CPU percentage drops to zero the moment it
# stops. The difference between those two numbers is the
# subject of the limits chapter.
end = time.time() + 4
while time.time() < end:
    pass
time.sleep(900)
