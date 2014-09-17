import socket, traceback

host = ''                               # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(8192)
        print("Got data from", address)
        # Acknowledge it.
        message = message.decode('utf8')
        message = message.upper()
        s.sendto(message.encode('utf8'), address)
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
