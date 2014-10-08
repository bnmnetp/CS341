# unreliable data transfer functions
# You may not modify either udt_send or udt_recv

import traceback
import socket
import random
import time
import pickle

# Probability of a message getting corrupted
CORRUPT_P = 0.3

# Probability of a message getting lost
LOST_P = 0.1

TIMEOUT = 3

DEBUG = True


##
## You may not modify anything below here
## 

class Packet: 
    def __init__(self,mess,seqnum,ip,port):
        self.is_corrupt = False
        self.mess = mess
        self.seqnum = seqnum
        self.ip = ip
        self.port = port


def make_pkt(mess,seqnum,ip,port):
    return Packet(mess,seqnum,ip,port)
    

def udt_send(pkt):
    '''
    Takes a Packet object as a parameter.
    This function returns the socket that was created and used to send the 
    message.  This socket should be passed to udt_recv.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # introduce fake propagatoin delay
    time.sleep(random.random())

    if random.random() <= LOST_P:
        if DEBUG:
            print("LOST PACKET ", pkt.seqnum)
        return s

    if random.random() <= CORRUPT_P:
        if DEBUG:
            print("sending a corrupt message in packet ", pkt.seqnum)
        pkt.is_corrupt = True
        pkt.mess = "XXX"
        pkt.seqnum = -1
    else:
        if DEBUG:
            print("sending a good message in packet ", pkt.seqnum)

    s.sendto(pickle.dumps(pkt), (pkt.ip,pkt.port))
    return s

def udt_recv(s):
    '''
    Takes the socket returned by udt_send
    returns the tuple (None, None) if there was a timeout
    otherwise returns a Packet object
    '''
    s.settimeout(TIMEOUT)
    try:
        data,addr = s.recvfrom(1024)
        pkt = pickle.loads(data)
        seqnum = pkt.seqnum
        return (pkt, addr)

    except socket.timeout:
        print("timeout in udt")
    except socket.error:
        traceback.print_exc()

    return (None,None)


# example of use with echoServer
if __name__ == '__main__':
    estring = input("-> ")
    while estring.lower() != "exit":
        pkt = make_pkt(estring,1,'',51423)
        sock = udt_send(pkt)
        pkt,addr = udt_recv(sock)
        if pkt:
            print(pkt.mess)
        else:
            print('got a timeout')


