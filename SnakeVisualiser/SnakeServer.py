import socket

server_port = int(input("Enter Server Port To Use: "))
client_port = int(input("Enter Client Port To Use: "))
client_ip = input("Enter Client IP: ")
client_number = input("Enter Client Number (0-5): ")


def get_head(msg):
    try:
        protocol_parts = msg.split("|")
        head_str = None
        if len(protocol_parts) > 1:
            snake_blocks = protocol_parts[1].split(";")
            if len(snake_blocks) > 1:
                head_str = snake_blocks[0]
        if head_str is not None:
            head_cords = head_str.split(',')
            if len(head_cords) > 1:
                if head_cords[0].isnumeric() and head_cords[1].isnumeric():
                    return [int(head_cords[0]), int(head_cords[1])]
    except Exception as error:
        print("Error in get_head: " + str(error))
    return [-1, -1]


def get_coords_of_all_snakes():
    global client_number
    coords_str = ""
    try:
        for i in range(5):
            if i != int(client_number):
                f = open("snakecoordinates/" + str(i) + ".txt", "r")
                protocol_parts = f.read().split("|")
                if len(protocol_parts) > 1:
                    coords_str = coords_str + protocol_parts[1]
            elif i == int(client_number):
                f = open("snakecoordinates/" + str(i) + ".txt", "r")
                protocol_parts = f.read().split("|")
                if len(protocol_parts) > 1:
                    snake_blocks_str = protocol_parts[1].split(";")
                    length = len(snake_blocks_str[0]) + len(snake_blocks_str[1]) + 2
                    coords_str = coords_str + protocol_parts[1][length:]
    except Exception as error:
        coords_str = ""
        print("Error in the getcoordsofallsnake: " + str(error))

    return coords_str


def convert_to_int_blocks(strng):
    snakes_blocks = []
    try:
        array = strng.split(";")

        for i in range(len(array)):
            blocks_str = array[i].split(',')
            if len(blocks_str) > 1:
                if blocks_str[0].isnumeric() and blocks_str[1].isnumeric():
                    snakes_blocks.append([int(blocks_str[0]), int(blocks_str[1])])
    except Exception as error:
        print("Error in the convert_to_int_blocks: " + str(error))
    return snakes_blocks


def check_collision(head, snakes_blocks):
    try:
        if len(head) > 1:
            if head[0] == -1 and head[1] == -1:
                return False
            for i in range(len(snakes_blocks)):
                if abs(int(head[0]) - int(snakes_blocks[i][0])) < 5 and abs(int(head[1]) - int(snakes_blocks[i][1])) < 5:
                    return True
    except Exception as error:
        print("Error in the getcoordsofallsnake: " + str(error))
    return False


welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('', server_port))

c1add = (client_ip, client_port)

msg1 = ""
gamestate = 'none'
result = ""
collided = False

while 1:
    try:
        cmsg, cadd = welcome_socket.recvfrom(1024)
        msg1 = cmsg.decode()
        name = msg1.split("|")[0]
        msg_to_send = ""
        head_cords = get_head(msg1)
        snakes_cords_str = get_coords_of_all_snakes()
        if check_collision(head_cords, convert_to_int_blocks(snakes_cords_str)):
            msg1 = name + "|0,0;|0,0,0,0,0"
            f = open("snakecoordinates/" + client_number + ".txt", "w")
            while f.closed:
                f = open("snakecoordinates/" + client_number + ".txt", "w")
            f.write(msg1)
            f.close()
            msg_to_send = "dead"
        else:
            client_info = None
            try:
                f = open("snakecoordinates/" + client_number + ".txt", "w")
                while f.closed:
                    f = open("snakecoordinates/" + client_number + ".txt", "w")
                f.write(msg1)
                f.close()
                for i in range(6):
                    if i != int(client_number):
                        f = open("snakecoordinates/" + str(i) + ".txt", "r")
                        while f.closed:
                            f = open("snakecoordinates/" + str(i) + ".txt", "r")
                        client_info = f.read()
                        split_client_info = client_info.split("|")
                        if len(split_client_info) > 1:
                            if not split_client_info[1] == "0,0;":
                                msg_to_send = msg_to_send + client_info + "\n"
                        f.close()
            except Exception as error:
                print("Error in else: " + str(error) + " client info: " + str(client_info))
        try:
            welcome_socket.sendto(msg_to_send.encode(), c1add)
        except Exception as error:
            print("Error in sendto socket: " + str(error))
    except Exception as error:
        print("Error in the tick: " + str(error))