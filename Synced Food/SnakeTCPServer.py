import socket
import random

def checkcollision():
    global msg1, msg2, gamestate
    array1 = []
    coord1 = msg1.split('|')[0]
    temparray = coord1.split(';')
    for i in range(len(temparray)):
        if len(temparray[i].split(","))>1:
            array1.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    array2 = []
    coord2 = msg2.split('|')[0]
    temparray = coord2.split(';')
    for i in range(len(temparray)):
        if len(temparray[i].split(","))>1:
            array2.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    head1 = array1[0]
    head2 = array2[0]
    for i in range(1,len(array1)):
        print(head2,array1[i])
        if abs(int(head2[0])-int(array1[i][0]))<10 and abs(int(head2[1])-int(array1[i][1]))<10:
            gamestate = 'msg1won'
            return 0
    for i in range(1,len(array2)):
        if abs(int(head1[0])-int(array2[i][0]))<10 and abs(int(head1[1])-int(array2[i][1]))<10:
            gamestate = 'msg2won'
            return 0
    gamestate = 'none'

time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('localhost',13000)
c2add = ('localhost',14000)

msg1 = ""
msg2 = ""
gamestate = 'none'

#nextcoord = random.randrange(30,500,10)+','+random.randrange(30,500,10)+','+random.randint(0,3)+''

while 1:
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        msg1 = cmsg
        if msg1 != "" and msg2 != "":
            checkcollision()
        if gamestate == 'none':
            welcome_socket.sendto(msg1.encode(), c2add)
        else:
            break
    else:
        msg2 = cmsg
        if msg1 != "" and msg2 != "":
            checkcollision()
        if gamestate == 'none':
            welcome_socket.sendto(msg2.encode(), c1add)
        else:
            break
