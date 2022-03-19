import socket
import random

a = int(input("Enter Server Port To Use: "))
b = int(input("Enter Client Port To Use: "))
d = input("Enter Client IP: ")
c = input("Enter Client Number (0-5): ")

def gethead(strng):
  head = strng.split(";")[0]
  return [int(head.split(',')[0]),int(head.split(',')[1])]

def getcoordsofallsnake():
  global c
  strng = ""
  for i in range(5):
    if i!=int(c):
      f = open("New/snakecoordinates/"+str(i)+".txt","r")
      coords = f.read().split("|")
      strng = strng + coords[0]
  
  return strng

def converttoarray(strng):
  retarray = []
  array = strng.split(";")
  for i in range(len(array)):
    if len(array[i].split(','))>1:
      retarray.append([int(array[i].split(",")[0]),int(array[i].split(",")[1])])
  
  return retarray

def checkcollision(head, snake):
    for i in range(len(snake)):
        if abs(int(head[0]) - int(snake[i][0])) < 5 and abs(int(head[1]) - int(snake[i][1])) < 5:
            return True
    return False

time1 = ''

server_port = a
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

welcome_socket.bind(('',server_port))

c1add = (d,b)#146.169.165.26

msg1 = ""
gamestate = 'none'
result = ""
collided = False



while 1:
    print('1')
    cmsg, cadd = welcome_socket.recvfrom(1024)
    print('2')  	
    msg1 = cmsg.decode()
    delivermsg = ""
    if checkcollision(gethead(msg1),converttoarray(getcoordsofallsnake())):
      collided = False
    if collided == True:
      msg1 = "0,0;|0,0,0,0,0"
      f = open("snakecoordinates/"+c+".txt","w")
      f.write(msg1)
      f.close()
      delivermsg = "dead"
    else:
      f = open("snakecoordinates/"+c+".txt","w")
      f.write(msg1)
      f.close()
      for i in range(5):
        if i!=int(c):
              f = open("snakecoordinates/"+str(i)+".txt","r")
              delivermsg = delivermsg + f.read() + "\n"
              f.close()
    print('3')            
    welcome_socket.sendto(delivermsg.encode(), c1add)
    print('4')
