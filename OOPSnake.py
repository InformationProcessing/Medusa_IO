import tkinter as tk
from tkinter import *
import time
import sys
import random
import os

root = tk.Tk()

time1 = ''
clock = Label(root)

canvas_width = 1000
canvas_height = 1000
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height,highlightthickness=3, highlightbackground="black")
canvas.pack()

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

    def addblock(self,i):
        self.moveblocks.append([0,-10])
        self.snake.append(canvas.create_rectangle(self.x,10*(len(self.snake)+1)+self.y,self.x+10,10*(len(self.snake)+1)+self.y+10,fill='gray'+str(len(self.snake)*2+1)))
        self.snakeblockscoordX.append(self.x) #vertical generation of the snake -> should look on how to make it general
        self.snakeblockscoordY.append(self.y-i*10)
        print("initialise: ", i, "----",self.snakeblockscoordX[i], "- ",self.snakeblockscoordY[i])

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
        def abs_move(new_x, new_y,j):
            # Get the current object position
            c_x = self.snakeblockscoordX[j] 
            c_y = self.snakeblockscoordY[j]
            # Move the object
            print("loop: ", j, "----",new_x-c_x, "- ",new_y-c_y," /x ", new_x, ",", c_x, " /y ", new_y, ",", c_y)
            canvas.move(self.snake[j], new_x-c_x, new_y-c_y)
            self.snakeblockscoordX[j] = new_x
            self.snakeblockscoordY[j] = new_y
            self.x = self.snakeblockscoordX[0]
            self.y = self.snakeblockscoordY[0]

        for j in range(len(self.moveblocks)-1,0,-1):
            self.moveblocks[j]=self.moveblocks[j-1]
            self.snakeblockscoordX[j]=self.snakeblockscoordX[j-1]
            self.snakeblockscoordY[j]=self.snakeblockscoordY[j-1]
            print("pos:", j, "----",self.snakeblockscoordX[j], ": ",self.snakeblockscoordY[j])
        self.moveblocks[0]=self.move
       

        print(self.x, " ", self.y)
        self.x = self.x + int(self.move[0])
        self.y = self.y + int(self.move[1])
        self.snakeblockscoordX[0]=self.x
        self.snakeblockscoordY[0]=self.y

        for j in range(len(self.moveblocks)):
            if self.snakeblockscoordX[j] < 0 or self.snakeblockscoordX[j] > 1000 or self.snakeblockscoordY[j] < 0 or self.snakeblockscoordY[j] > 1000:
                if  self.snakeblockscoordX[j] < 0:     abs_move(1000,self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordX[j] > 1000:  abs_move(0,   self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordY[j] < 0:     abs_move(self.snakeblockscoordX[j],1000,j)
                if  self.snakeblockscoordY[j] > 1000:  abs_move(self.snakeblockscoordX[j],   0,j)
            else:
                print(j, "----",self.moveblocks[j][0], "- ",self.moveblocks[j][1])
                canvas.move(self.snake[j],self.moveblocks[j][0],self.moveblocks[j][1])
            # print(self.moveblocks[0][0], "- ",self.moveblocks[0][1])

        # if self.y < 0: self.y = 1000
        # elif self.y > 1000: self.y = 0
        # if self.x < 0: self.x = 1000
        # elif self.x > 1000: self.x = 0





    def adjustspeed(self,speed):
        self.speed = speed

    def getspeed(self):
        return self.speed


player = Snake(500, 500)

for i in range(10):
    player.addblock(i)

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

button1 = tk.Button(text='Increase Speed',command=increasespeed)
canvas.create_window(270,18,window=button1)
button2 = tk.Button(text='Decrease Speed',command=decreasespeed)
canvas.create_window(100,18,window=button2)

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    player.movesnake()
    clock.after(int(100/(player.getspeed())),tick)

root.bind("<Key>",kpress)
tick()
root.mainloop()
