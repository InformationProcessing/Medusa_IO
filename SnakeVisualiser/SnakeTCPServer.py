import socket
import random

a = int(input("Enter Server Port To Use: "))
b = int(input("Enter Client Port To Use: "))
c = input("Enter Client Number (0-5): ")

time1 = ''

server_port = a
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('localhost',b)#146.169.165.26

msg1 = ""
gamestate = 'none'
result = ""

while 1:
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    msg1 = cmsg.decode()
    f = open("snakecoordinates/"+c+".txt","w")
    f.write(msg1)
    f.close()
    
    delivermsg = ""
    for i in range(5):
      if i!=int(c):
            f = open("New/snakecoordinates/"+str(i)+".txt","r")
            delivermsg = delivermsg + f.read() + "\n"
            f.close()
                 
    welcome_socket.sendto(delivermsg.encode(), c1add)
