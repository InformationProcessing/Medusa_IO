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
      msg = ""
      for i in range(len(player.snakeblockscoordX)):
            msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect(('localhost',12002)) 
      client_socket.send(msg.encode())
      client_socket.close()

def tick(player,found):
    global time1
    global food
    global otherplayer
    global otherplayerblocks
    time2 = time.strftime('%H:%M:%S')
    
    sendCoord()
    
    for i in range(len(otherplayerblocks)):
          SnakeGameMap.canvas.delete(otherplayerblocks[i])

    otherplayer=[mergearray(player.snakeblockscoordX,player.snakeblockscoordY)]#should be coordinates taken from tcp

    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    player.movesnake()
    
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
