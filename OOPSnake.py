import tkinter as tk
from tkinter import *
import time
import sys
import random
import os

root = tk.Tk()

time1 = ''
clock = Label(root)

canvas_width = 700
canvas_height = 700
canvas = tk.Canvas(root, width = canvas_width+1, height = canvas_height+1, highlightthickness=10, highlightbackground="black")
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
        for i in range(10):
            self.addblock(i)

    def addblock(self,i):
        self.moveblocks.append([0,-10])
        block=tk.Canvas(canvas,width=10, height=10, bd=0, highlightthickness=0, relief='ridge', bg="gray"+str(i*3))
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
        def abs_move(new_x, new_y,j):
            self.snake[j].place(x=new_x, y=new_y)
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
        for j in range(len(self.snake)):
            if self.snakeblockscoordX[j] < 10 or self.snakeblockscoordX[j] > canvas_width or self.snakeblockscoordY[j] < 10 or self.snakeblockscoordY[j] > canvas_height:
                if  self.snakeblockscoordX[j] < 10:              abs_move(canvas_width, self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordX[j] > canvas_width:   abs_move(10,            self.snakeblockscoordY[j],j)
                if  self.snakeblockscoordY[j] < 10:              abs_move(self.snakeblockscoordX[j],canvas_height,j)
                if  self.snakeblockscoordY[j] > canvas_height:  abs_move(self.snakeblockscoordX[j],            10,j)
            else:
                print(j, "----",self.moveblocks[j][0], "- ",self.moveblocks[j][1])
                self.snake[j].place(x=self.snakeblockscoordX[j], y=self.snakeblockscoordY[j])

        self.x = self.x + int(self.moveblocks[0][0])
        self.y = self.y + int(self.moveblocks[0][1])
        self.snakeblockscoordX[0]=self.x
        self.snakeblockscoordY[0]=self.y





    def adjustspeed(self,speed):
        self.speed = speed

    def getspeed(self):
        return self.speed


player = Snake(500, 500)


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
