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
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

class Snake:
    snake = []
    x = 0
    y = 0
    move = [0,-10]
    moveblocks = []
    speed = 1
    
    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord

    def addblock(self):
        self.moveblocks.append([0,-10])
        self.snake.append(canvas.create_rectangle(self.x,10*(len(self.snake)+1)+self.y,self.x+10,10*(len(self.snake)+1)+self.y+10,fill='gray'+str(len(self.snake)*2+1)))

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
        for j in range(len(self.moveblocks)-1,0,-1):
            self.moveblocks[j]=self.moveblocks[j-1]
        self.moveblocks[0]=self.move
        for j in range(len(self.moveblocks)):
            canvas.move(self.snake[j],self.moveblocks[j][0],self.moveblocks[j][1])
        print(self.move)
        self.x = self.x + int(self.move[0])
        self.y = self.y + int(self.move[1])
        if self.y < 0 or self.y>1000 or self.x<0 or self.x>1000:
            sys.exit()
                
    def adjustspeed(self,speed):
        self.speed = speed

    def getspeed(self):
        return self.speed


player = Snake(500, 500)

for i in range(10):
    player.addblock()

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
