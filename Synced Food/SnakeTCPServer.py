import socket
import random

time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('localhost',13000)
c2add = ('localhost',14000)

msg1 = ""
msg2 = ""

#nextcoord = random.randrange(30,500,10)+','+random.randrange(30,500,10)+','+random.randint(0,3)+''

while 1:
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        msg1 = cmsg
        welcome_socket.sendto(msg1.encode(), c2add)
    else:
        msg2 = cmsg
        welcome_socket.sendto(msg2.encode(), c1add)