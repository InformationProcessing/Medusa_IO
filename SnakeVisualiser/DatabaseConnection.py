import socket
import time

def connect():
    print("Connecting to datatbase...")
    server_name = '184.73.88.253' # ALex's EC2 ip (need to run the tcp server manually)
    server_port = 13000
    #create a TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    msg = "username, totalscore, highestscore, kills"
    f = open("./snakecoordinates/localscores.txt","r")
    msg = f.read()
    f.close()
    print(msg)

    currtime = time.time()

    #send the message to the TCP server
    client_socket.send(msg.encode())
    msg = client_socket.recv(4096) 
    after_received = time.time()
    print("Duration = ",after_received-currtime)

    print(msg.decode())
    f = open("./snakecoordinates/leaderboards.txt","w")
    f.write(msg.decode())
    f.close()

    client_socket.close() 
    #  Teodora,a75,18,10,44; lollycraft,a75,15,8,21; vpnum,a75,3,9,29