import tkinter as tk
from tkinter import *
import time
import sys
import random
import os
import socket
import SnakeGameMap
import subprocess
import sys
import atexit

a = int(input("Enter Your Port:"))
b = int(input("Enter Server Port:"))
c = input("Enter Server IP: ")

client_port = a

time1 = ''
clock = Label(SnakeGameMap.root)

otherplayer = []
otherplayerblocks=[]

def exit_handler():
      msg = "0,0;|0,0,0,0,0"
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      client_socket.bind(('', client_port))
      client_socket.sendto(msg.encode(),(c,b))
      
atexit.register(exit_handler)

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

def mergearray(array1,array2):
      newarray=[]
      for i in range(len(array1)):
            newarray.append([array1[i]+100,array2[i]+100])
      return newarray

player = SnakeGameMap.player
# playerShadow = SnakeGameMap.snakeShadow
food = SnakeGameMap.sharedFood
localFood = SnakeGameMap.localFood
wefoundfood = 0
_x = 0
_y = 0
_r = 0
_j = 0

def sendCoord():
      global client_port, wefoundfood, b
      msg = ""
      for i in range(len(player.snakeblockscoordX)):
            msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
      msg = msg + "|" + str(_x) + "," + str(_y) + "," + str(_r) + "," + str(_j) + "," + str(wefoundfood)
      wefoundfood = 0
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      client_socket.bind(('',my_port))
      client_socket.sendto(msg.encode(),(c,b))
      msg, sadd = client_socket.recvfrom(2048)
      
      if msg.decode() == "dead":
            #Client is DEAD
            quit()
            
      users = msg.decode().split("\n")
      message = []
      foodinfo = []
      
      for i in range(len(users)):
            if len(users[i].split('|'))>1:
                  message.append(users[i].split('|')[0])
                  foodinfo.append(users[i].split('|')[1])
                  
      for i in range(len(foodinfo)):
            tempfood = foodinfo[i].split(",")
            if tempfood[4]=='1':
                  global food
                  food.deleteShared()
                  food.generateShared(int(tempfood[0]), int(tempfood[1]))
                  food.generateShared(int(tempfood[0]), int(tempfood[1]))
      
      return message

def deleteblocks():
      global otherplayerblocks
      for i in range(len(otherplayerblocks)):
            SnakeGameMap.canvas.delete(otherplayerblocks[i])

def updateothers():
      global otherplayer
      global otherplayerblocks
      for i in range(len(otherplayer)):
              for j in range(len(otherplayer[i])):
                    otherplayerblocks.append(SnakeGameMap.canvas.create_rectangle(int(otherplayer[i][j][0]),int(otherplayer[i][j][1]),int(otherplayer[i][j][0])+10,int(otherplayer[i][j][1])+10,fill='#C7FFFD'))
      

def tick(player,found):
      
    deleteblocks()    
    global time1
    global food
    global localFood
    global otherplayer
    global otherplayerblocks
    global wefoundfood
    global _x,_y,_r,_j
    time2 = time.strftime('%H:%M:%S')
    
    msg = sendCoord()
    array = []
    for i in range(len(msg)):
            temparray = msg[i].split(";")
            for j in range(len(temparray)):
                  if len(temparray[j])>0:
                        array.append([temparray[j].split(",")[0],temparray[j].split(",")[1]])
    otherplayer=[array] 

    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    player.movesnake()
#     if player.shadowCreated == True:
#         playerShadow.moveShadow()
    
    updateothers()
    
    if (abs(player.x - food.shared_power_upX)<food.radius and abs(player.y - food.shared_power_upY)<food.radius):
            player.adjustspeed(1)
            food.powerupType(player,"Ultra-Power")
            food.deleteShared()
            _x = random.randrange(30,500,10)
            _y = random.randrange(20,500,10)
            food.generateShared(_x,_y)
            wefoundfood = 1
            
      
    for i in range (0, len(localFood.power_ups)):
        if (player.x == localFood.power_upsX[i]) and (player.y == localFood.power_upsY[i]):
            player.adjustspeed(1)
            localFood.powerupType(player,localFood.power_ups[i][1])
            clock.after(200,lambda: tick(player,FALSE)) 
            localFood.delete(i)
            localFood.generate()
            found = TRUE
            break

    if found == FALSE : clock.after(int(100/player.getspeed()),lambda: tick(player,FALSE))



SnakeGameMap.root.bind("<Key>",SnakeGameMap.kpress)
try:
      tick(player,FALSE)
except:
      print("error, try - catch")
SnakeGameMap.root.mainloop()
