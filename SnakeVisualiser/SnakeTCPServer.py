import socket

msg1 = ""
msg2 = ""
game_state = None


def convert_snake_coords_to_array(coord_str):
    result = []
    coords = coord_str.split(';')
    for i in range(len(coords)):
        if len(coords[i].split(",")) > 1:
            result.append([coords[i].split(",")[0], coords[i].split(",")[1]])
    return result


def did_head_collide(head, snake):
    for i in range(1, len(snake)):
        if abs(int(head[0]) - int(snake[i][0])) < 5 and abs(int(head[1]) - int(snake[i][1])) < 5:
            return True
    return False


def check_collision():
    coord1 = msg1.split('|')[0]
    coord2 = msg2.split('|')[0]
    snake1 = convert_snake_coords_to_array(coord1)
    snake2 = convert_snake_coords_to_array(coord2)
    head1 = snake1[0]
    head2 = snake2[0]
    if did_head_collide(head2, snake1):
        return 'snake1won'
    elif did_head_collide(head1, snake2):
        return 'snake2won'


time1 = ''

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('', server_port))

c1add = ('localhost', 13000)  # 146.169.165.26
c2add = ('localhost', 14000)

result = ""

# nextcoord = random.randrange(30,500,10)+','+random.randrange(30,500,10)+','+random.randint(0,3)+''

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
        else:
            print("Unknown client connected")
    except Exception as e:
        print("Error occurred: " + str(e))