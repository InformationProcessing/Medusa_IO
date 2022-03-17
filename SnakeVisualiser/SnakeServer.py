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
        if abs(int(head2[0])-int(array1[i][0]))<5 and abs(int(head2[1])-int(array1[i][1]))<5:
            gamestate = 'msg1won'
            return 0
    for i in range(1,len(array2)):
        if abs(int(head1[0])-int(array2[i][0]))<5 and abs(int(head1[1])-int(array2[i][1]))<5:
            gamestate = 'msg2won'
            return 0
    gamestate = 'none'

time1 = ''

server_port = 12010
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('146.169.192.141', 514)#146.169.165.26
c2add = ('localhost',14000)

msg1 = ""
msg2 = ""
msg3 = ""
gamestate = 'none'
result = ""

#nextcoord = random.randrange(30,500,10)+','+random.randrange(30,500,10)+','+random.randint(0,3)+''

while 1:
    try:
        cmsg, cadd = welcome_socket.recvfrom(2048)
        cmsg = cmsg.decode()
        if cadd[1] == 514:
            msg1 = cmsg
            c1connected = True

            if saved_message_dest == 'Client 1':
                welcome_socket.sendto(saved_message.encode(), c1add)
                saved_message = None
                saved_message_dest = None

            if c2connected:
                if msg1 != "" and msg2 != "":
                    game_state = check_collision()
                if game_state is None:
                    welcome_socket.sendto(msg1.encode(), c2add)
                else:
                    welcome_socket.sendto(game_state.encode(), c2add)
                    welcome_socket.sendto(game_state.encode(), c1add)
            else:
                saved_message = cmsg
                saved_message_dest = 'Client 2'
        elif cadd[1] == 14000:
            msg2 = cmsg
            c2connected = True

            if saved_message_dest == 'Client 2':
                welcome_socket.sendto(saved_message.encode(), c2add)
                saved_message = None
                saved_message_dest = None

            if c1connected:
                if msg1 != "" and msg2 != "":
                    game_state = check_collision()
                if game_state is None:
                    welcome_socket.sendto(msg2.encode(), c1add)
                else:
                    welcome_socket.sendto(game_state.encode(), c1add)
                    welcome_socket.sendto(game_state.encode(), c2add)
            else:
                saved_message = cmsg
                saved_message_dest = 'Client 1'
    cmsg, cadd = welcome_socket.recvfrom(2048)
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        msg1 = cmsg
        print(msg1)
        if msg1 != "" and msg2 != "":
            checkcollision()
        if gamestate != 'msg1won':
            welcome_socket.sendto(msg1.encode(), c2add)
        else:
            welcome_socket.sendto(gamestate.encode(), c2add)
            welcome_socket.sendto(gamestate.encode(), c1add)
    else:
        msg2 = cmsg
        if msg1 != "" and msg2 != "":
            checkcollision()
        if gamestate != 'msg2won':
            welcome_socket.sendto(msg2.encode(), c1add)
        else:
            welcome_socket.sendto(gamestate.encode(), c2add)
            welcome_socket.sendto(gamestate.encode(), c1add)