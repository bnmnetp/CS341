# Echo client program
import socket

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server

estring = input("-> ")
while estring.lower() != "exit":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(estring.encode('utf8'))  # encode needed in Python3
    data = s.recv(1024)
    print("result = ", data.decode('utf8'))  # decode needed in Python3
    estring = input("-> ")
    s.close()
