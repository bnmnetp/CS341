import socket, traceback
from udt import *

host = ''                               # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    try:
        #message, address = s.recvfrom(8192)
        pkt,address = udt_recv(s)
        if pkt:
            print("Got data from", address, pkt.mess)
            pkt.mess = pkt.mess.upper()
            pkt.ip = address[0]
            pkt.port = address[1]
            udt_send(pkt)
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
