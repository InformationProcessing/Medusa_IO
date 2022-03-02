import tkinter as tk
from tkinter import *
import time
import sys
import random
import os
import socket
import SnakeGameMap


time1 = ''
clock = Label(SnakeGameMap.root)
my_port = 14000

otherplayer = []
otherplayerblocks=[]

def mergearray(array1,array2):
      newarray=[]
      for i in range(len(array1)):
            newarray.append([array1[i]+100,array2[i]+100])
      return newarray

player = SnakeGameMap.player
food = SnakeGameMap.food

def sendCoord():
      global my_port
      msg = ""
      for i in range(len(player.snakeblockscoordX)):
            msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      client_socket.bind(('',my_port))
      client_socket.sendto(msg.encode(),('localhost',12001))
      
      msg, sadd = client_socket.recvfrom(2048)
      msg = msg.decode()
      return msg

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
      


def tick(player,found):
    deleteblocks()    
    global time1
    global food
    global otherplayer
    global otherplayerblocks
    time2 = time.strftime('%H:%M:%S')
    
    msg = sendCoord()
    #print(msg)
    
    array = []
    temparray = msg.split(";")
    
    for i in range(len(temparray)):
        if len(temparray[i])>2:
            array.append([temparray[i].split(",")[0],temparray[i].split(",")[1]])
    
    otherplayer=[array]

    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    player.movesnake()
    
    updateothers()
    for j in range (len(food.power_ups)):
        if (player.x == food.power_upsX[j]) and (player.y == food.power_upsY[j]):
            #   print("Player's pos:",player.x,player.y)
            #   print("Food Pos: ",food.xcoord,food.ycoord) 
            # foodTypes = ["grow", "portal", "ultra_speed"]
            player.adjustspeed(1)
            # food.powerupType(player,"portal")
            food.powerupType(player,food.power_ups[j][1])
            clock.after(100,lambda: tick(player,FALSE)) 
            food.delete(j)
            food.generate()
            found = TRUE
            break #not necesarry? but agree that is good for optimisation

    if found == FALSE : clock.after(int(100/player.getspeed()),lambda: tick(player,FALSE))



SnakeGameMap.root.bind("<Key>",SnakeGameMap.kpress)
tick(player,FALSE)
SnakeGameMap.root.mainloop()