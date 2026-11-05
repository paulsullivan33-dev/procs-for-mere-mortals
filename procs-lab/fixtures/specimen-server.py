import socket, time
# Specimen: listens on 127.0.0.1:18089 and then just sleeps.
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 18089))
s.listen(5)
time.sleep(900)
