import socket
import random

time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('', server_port))

c1add = ('localhost', 13000)
c2add = ('localhost', 14000)

msg1 = ""
msg2 = ""

c1connected = False
c2connected = False
saved_message = None
saved_message_dest = None

# nextcoord = random.randrange(30,500,10)+','+random.randrange(30,500,10)+','+random.randint(0,3)+''

while 1:
    print("While")
    try:
        cmsg, cadd = welcome_socket.recvfrom(2048)
        cmsg = cmsg.decode()

        print("Message: " + cmsg + " from client: " + str(cadd[0]) + " " + str(cadd[1]))
        if cadd[1] == 13000:
            msg1 = cmsg
            c1connected = True

            if saved_message_dest == 'Client 1':
                welcome_socket.sendto(saved_message.encode(), c1add)

            if c2connected:
                welcome_socket.sendto(msg1.encode(), c2add)
            else:
                saved_message = cmsg
                saved_message_dest = 'Client 2'
        elif cadd[1] == 14000:
            msg2 = cmsg
            c2connected = True

            if saved_message_dest == 'Client 2':
                welcome_socket.sendto(saved_message.encode(), c2add)

            if c1connected:
                welcome_socket.sendto(msg2.encode(), c1add)
            else:
                saved_message = cmsg
                saved_message_dest = 'Client 1'
        else:
            print("Unknown client connected")
    except:
        print("Error occurred.")
