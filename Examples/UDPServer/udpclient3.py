import socket, sys, time, traceback

host = sys.argv[1]    # get hostname from command line
textport = "51423"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)

print ("Enter data to transmit: ")
data = sys.stdin.readline().strip()
s.sendto(data,(host,port))

#print "Looking for replies; press Ctrl-C or Ctrl-Break to stop"
while True:
    buf,addr = s.recvfrom(2048)
    print ('got data back from: ', addr)
    if not len(buf):
        break
    print("Received: %s" % buf.decode('utf8'))
    try:
        data = sys.stdin.readline().strip()   # readline returns bytes
        s.sendto(data,(host,port))
    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
        break

s.shutdown(1)
