import socket
import time


#  Teodora,a75,18,10,44; lollycraft,a75,15,8,21; vpnum,a75,3,9,29
def update_score(username, total_score, kills):
    print("Connecting to database...")
    server_name = '184.73.88.253'  # ALex's EC2 ip (need to run the tcp server manually)
    server_port = 13000
    # create a TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    msg = username + ", a75," + str(total_score) + ", " + str(kills)
    print("Message to send to DB: " + msg)

    currtime = time.time()

    # send the message to the TCP server
    client_socket.send(msg.encode())
    msg = client_socket.recv(4096)
    client_socket.close()

    after_received = time.time()
    print("Duration = ", after_received - currtime)

    received_message = msg.decode()
    print("Received message: " + received_message)

    return received_message
