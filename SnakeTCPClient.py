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

# canvas_width = 700
# canvas_height = 700
# canvas = tk.Canvas(root, width = canvas_width+1, height = canvas_height+1, highlightthickness=10, highlightbackground="black")
# canvas.pack()

otherplayer = []
otherplayerblocks=[]

def mergearray(array1,array2):
      newarray=[]
      for i in range(len(array1)):
            newarray.append([array1[i]+100,array2[i]+100])
      return newarray

player = SnakeGameMap.Snake(500, 500)
food = SnakeGameMap.powerup()

def sendCoord():
      msg = ""
      for i in range(len(player.snakeblockscoordX)):
            msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect(('localhost',12002)) 
      client_socket.send(msg.encode())
      client_socket.close()

def tick(player):
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
    
    if (player.x == food.xcoord) and (player.y == food.ycoord):
          print("Player's pos:",player.x,player.y)
          print("Food Pos: ",food.xcoord,food.ycoord) 
          food.move()
          player.addblock(len(player.snake)+1)
          animation = "blue"
          SnakeGameMap.snakeAnnimation(player,animation)
          animation = "return"
          SnakeGameMap.snakeAnnimation(player,animation)
          clock.after(int(100/player.getspeed()),lambda: tick(player))
      
    else:
        clock.after(int(100/player.getspeed()),lambda: tick(player))



root.bind("<Key>",SnakeGameMap.kpress)
tick(SnakeGameMap.player)
root.mainloop()