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

while 1:
    try:
        cmsg, cadd = welcome_socket.recvfrom(2048)
        cmsg = cmsg.decode()

        if cadd[1] == 13000:
            msg1 = cmsg
            c1connected = True

            if saved_message_dest == 'Client 1':
                welcome_socket.sendto(saved_message.encode(), c1add)
                saved_message = None
                saved_message_dest = None

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
                saved_message = None
                saved_message_dest = None

            if c1connected:
                welcome_socket.sendto(msg2.encode(), c1add)
            else:
                saved_message = cmsg
                saved_message_dest = 'Client 1'
        else:
            print("Unknown client connected")
    except Exception as e:
        print("Error occurred: " + str(e))
