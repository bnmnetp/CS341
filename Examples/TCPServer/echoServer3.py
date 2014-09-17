# Echo server program
import socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
QUEUELEN = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(QUEUELEN)

while 1:
    conn, addr = s.accept()  # blocks here
    print('Connected by', addr)
    data = conn.recv(1024)
    strdata = data.decode('utf8')  # decode needed in Python3
    if not data: break
    data = strdata.upper().encode('utf8')  # encode needed in Python3
    conn.send(data)
    conn.close()
