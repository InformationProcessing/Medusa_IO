import tkinter as tk
from tkinter import *
import time
import sys
import random
import os
import socket
import SnakeGameMap

root = tk.Tk()
time1 = ''
clock = Label(root)

server_port = 12002
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcome_socket.bind(('localhost',server_port))
welcome_socket.listen(1)

otherplayer = []

def mergearray(array1,array2):
      newarray=[]
      for i in range(len(array1)):
            newarray.append([array1[i]+100,array2[i]+100])
      return newarray

otherplayerblocks=[]

def deleteblocks():
      global otherplayerblocks
      for i in range(len(otherplayerblocks)):
          SnakeGameMap.canvas.delete(otherplayerblocks[i])

def updateothers():
      global otherplayer
      global otherplayerblocks
      for i in range(len(otherplayer)):
              for j in range(len(otherplayer[i])):
                    otherplayerblocks.append(SnakeGameMap.canvas.create_rectangle(int(otherplayer[i][j][0]),int(otherplayer[i][j][1]),int(otherplayer[i][j][0])+10,int(otherplayer[i][j][1])+10))

while 1:
#     global otherplayer
#     global time1
#     global food
    
    time2 = time.strftime('%H:%M:%S')
    print(otherplayer)
    
    #Deletes all previous blocks from last cycle, so it doesnt replicate
    deleteblocks()
    
    #Gets new 2d array from TCP
#     global server_port
#     global welcome_socket
    print('Server running on port ', server_port)
    connection_socket, caddr = welcome_socket.accept()
    cmsg = connection_socket.recv(1024)  	
    cmsg = cmsg.decode()
    
    msg = cmsg
    array=[]
    temparray = msg.split(";")
    
    for i in range(len(temparray)):
        if len(temparray[i])>2:
            array.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    
    otherplayer=[array]

    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
#     player.movesnake()

    #Updates Other Player Blocks 
    updateothers()
    
#     for j in range (len(food.power_ups)):
#         if (player.x == food.power_upsX[j]) and (player.y == food.power_upsY[j]):
#             #   print("Player's pos:",player.x,player.y)
#             #   print("Food Pos: ",food.xcoord,food.ycoord) 
#             # foodTypes = ["grow", "portal", "ultra_speed"]
#             player.adjustspeed(1)
#             # food.powerupType(player,"portal")
#             food.powerupType(player,food.power_ups[j][1])
#             clock.after(100,lambda: tick(player,FALSE)) 
#             food.delete(j)
#             food.generate()
#             found = TRUE
#             break #not necesarry? but agree that is good for optimisation

#     if found == FALSE : clock.after(int(100/player.getspeed()),lambda: tick(player,FALSE))


    
# player = SnakeGameMap.Snake(200,200)
# food = SnakeGameMap.food

# SnakeGameMap.root.bind("<Key>",SnakeGameMap.kpress)
# tick()
# SnakeGameMap.root.mainloop()
print('done')
