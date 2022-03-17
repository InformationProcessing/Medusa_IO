import socket
import random

server_port = int(input("Enter Server Port To Use: "))
client_port = int(input("Enter Client Port To Use: "))
client_number = input("Enter Client Number (0-5): ")


def gethead(strng):
    head = strng.split(";")[0]
    return [int(head.split(',')[0]), int(head.split(',')[1])]


def getcoordsofallsnake():
    global client_number
    strng = ""
    for i in range(5):
        if i != int(client_number):
            f = open("snakecoordinates/" + str(i) + ".txt", "r")
            coords = f.read().split("|")
            strng = strng + coords[0]

    return strng


def converttoarray(strng):
    retarray = []
    array = strng.split(";")
    for i in range(len(array)):
        if len(array[i].split(',')) > 1:
            retarray.append([int(array[i].split(",")[0]), int(array[i].split(",")[1])])

    return retarray


def checkcollision(head, snake):
    for i in range(len(snake)):
        if abs(int(head[0]) - int(snake[i][0])) < 5 and abs(int(head[1]) - int(snake[i][1])) < 5:
            return True
    return False


time1 = ''

welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('', server_port))

c1add = ('localhost', client_port)  # 146.169.165.26

msg1 = ""
gamestate = 'none'
result = ""
collided = False
counter = 0
while 1:
    cmsg, cadd = welcome_socket.recvfrom(2048)
    counter = counter + 1
    msg1 = cmsg.decode()
    msg_to_send = ""
    if checkcollision(gethead(msg1), converttoarray(getcoordsofallsnake())):
        collided = True
    if collided or counter > 100:
        msg1 = "0,0;|0,0,0,0,0"
        f = open("snakecoordinates/" + client_number + ".txt", "w")
        f.write(msg1)
        f.close()
        msg_to_send = "dead"
    else:
        f = open("snakecoordinates/" + client_number + ".txt", "w")
        f.write(msg1)
        f.close()
        for i in range(5):
            if i != int(client_number):
                f = open("snakecoordinates/" + str(i) + ".txt", "r")
                client_info = f.read()
                split_client_info = client_info.split("|")
                if not split_client_info[1] == "0,0;":
                    msg_to_send = msg_to_send + client_info + "\n"
                f.close()

    welcome_socket.sendto(msg_to_send.encode(), c1add)
