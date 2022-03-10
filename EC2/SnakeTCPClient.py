import tkinter as tk
from tkinter import *
import time
import sys
import random
import os
import socket


root = tk.Tk()

time1 = ''
clock = Label(root)

canvas_width = 700
canvas_height = 700
canvas = tk.Canvas(root, width = canvas_width+1, height = canvas_height+1, highlightthickness=10, highlightbackground="black")
canvas.pack()

otherplayer = []
otherplayerblocks=[]

def mergearray(array1,array2):
      newarray=[]
      for i in range(len(array1)):
            newarray.append([array1[i]+100,array2[i]+100])
      return newarray

class Snake:
    snake = []
    snakeblockscoordX = []
    snakeblockscoordY = []
    x = 0
    y = 0
    move = [0,-10]
    moveblocks = []
    speed = 1
    
    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord
        for i in range(10):
            self.addblock(i)

    def addblock(self,i):
        self.moveblocks.append([0,0])
        block=tk.Canvas(canvas,width=10, height=10, bd=0, highlightthickness=0.5, highlightbackground="white", relief='ridge', bg="gray"+str((i*3)%100))
        block.place(x=self.x, y=self.y-i*10)
        self.snake.append(block)
        self.snakeblockscoordX.append(self.x)
        self.snakeblockscoordY.append(self.y-i*10)
        # print("initialise: ", i, "----",self.snakeblockscoordX[i], "- ",self.snakeblockscoordY[i])

    def changedir(self,dir1):
        if dir1=='Up':
            self.move = [0,-10]
        elif dir1=='Left':
            self.move = [-10,0]
        elif dir1=='Down':
            self.move = [0,10]
        elif dir1=='Right':
            self.move = [10,0]
        
    def movesnake(self):
        #special teleportation of a block
        def abs_move(new_x, new_y,j):
            self.snake[j].place(x=new_x, y=new_y)
            self.snakeblockscoordX[j] = new_x
            self.snakeblockscoordY[j] = new_y
            self.x = self.snakeblockscoordX[0]
            self.y = self.snakeblockscoordY[0]

        #passing on block movement orientation.step to the following block
        for j in range(len(self.moveblocks)-1,0,-1):
            self.moveblocks[j]=self.moveblocks[j-1]
            self.snakeblockscoordX[j]=self.snakeblockscoordX[j-1]
            self.snakeblockscoordY[j]=self.snakeblockscoordY[j-1]
            print("pos:", j, "----",self.snakeblockscoordX[j], ": ",self.snakeblockscoordY[j])
        self.moveblocks[0]=self.move
        #blocking moving backwards and overlapping snake
        if self.moveblocks[0][0] == -self.moveblocks[1][0]:
            self.moveblocks[0][0] = self.moveblocks[1][0]
        if self.moveblocks[0][1] == -self.moveblocks[1][1]:
            self.moveblocks[0][1] = self.moveblocks[1][1]

        print(self.x, " ", self.y)
        #for every block in the snake, move or teleport
        for j in range(len(self.snake)):
            if self.snakeblockscoordX[j] < 10 or self.snakeblockscoordX[j] > canvas_width or self.snakeblockscoordY[j] < 10 or self.snakeblockscoordY[j] > canvas_height:
                if  self.snakeblockscoordX[j] < 10:             abs_move(canvas_width, self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordX[j] > canvas_width:   abs_move(10,            self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordY[j] < 10:             abs_move(self.snakeblockscoordX[j],canvas_height,j)
                if  self.snakeblockscoordY[j] > canvas_height:  abs_move(self.snakeblockscoordX[j],            10,j)
            else:
                # print(j, "----",self.moveblocks[j][0], "- ",self.moveblocks[j][1])
                self.snake[j].place(x=self.snakeblockscoordX[j], y=self.snakeblockscoordY[j])

        self.x = self.x + int(self.moveblocks[0][0])
        self.y = self.y + int(self.moveblocks[0][1])
        self.snakeblockscoordX[0]=self.x
        self.snakeblockscoordY[0]=self.y

    def adjustspeed(self,speed):
        self.speed = speed

    def getspeed(self):
        return self.speed


class powerup:
        xcoord = 0
        ycoord = 0
        id = 0 #= canvas.create_oval(500,500,500+6,500+6,fill='blue',tag="test")
        #the id of food is a necessary parameter to have as it can be called
        #simply can just create a new oval or new parameter rather than whole new class
        def __init__(self):
            x = random.randrange(30,500,10)
            y = random.randrange(20,500,10) #using random num_gen for food. 
            self.id = canvas.create_oval(x,y+5,x+5,y+10,fill='blue',tag="test")
            self.xcoord=x
            self.ycoord=y
        def move(self):
            x = random.randrange(30,500,10)
            y = random.randrange(20,500,10) #using random num_gen for food.
            canvas.delete("test")
            self.id = canvas.create_oval(x,y+5,x+5,y+10,fill='blue',tag="test")
            self.xcoord=x
            self.ycoord=y


player = Snake(500, 500)
food = powerup()

def kpress(event):
      if event.keysym == 'Up':
            player.changedir('Up')
            
      if event.keysym == 'Left':
            player.changedir('Left')
            
      if event.keysym == 'Down':
            player.changedir('Down')
            
      if event.keysym == 'Right':
            player.changedir('Right')


def increasespeed():
    if player.getspeed()!=100:
        player.adjustspeed(player.getspeed()+1)

def decreasespeed():
    if player.getspeed()!=1:
        player.adjustspeed(player.getspeed()-1)

def snakeAnnimation( player,animation ):
    if animation == "blue":
        for j in range(len(player.snake)):
            player.snake[j].configure(bg="blue")
    elif animation == "return":
        for j in range(len(player.snake)):
            player.snake[j].configure(bg="gray"+str(j*3))


button1 = tk.Button(text='Increase Speed',command=increasespeed)
canvas.create_window(270,18,window=button1)
button2 = tk.Button(text='Decrease Speed',command=decreasespeed)
canvas.create_window(100,18,window=button2)

def sendCoord():
      msg = ""
      for i in range(len(player.snakeblockscoordX)):
            msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
      file = open("input.txt","w")
      file.write(msg)
      file.close()
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
          canvas.delete(otherplayerblocks[i])

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
          snakeAnnimation(player,animation)
          animation = "return"
          snakeAnnimation(player,animation)
          clock.after(int(100/player.getspeed()),lambda: tick(player))
      
    else:
        clock.after(int(100/player.getspeed()),lambda: tick(player))



root.bind("<Key>",kpress)
tick(player)
root.mainloop()