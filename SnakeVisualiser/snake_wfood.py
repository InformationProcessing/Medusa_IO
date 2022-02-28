import tkinter as tk
from tkinter import *
import time
import sys
import random

root = tk.Tk()

time1 = ''
clock = Label(root)

canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def kpress(event):
      if event.keysym == 'Up':
            player.changedir('Up')
            
      if event.keysym == 'Left':
            player.changedir('Left')
            
      if event.keysym == 'Down':
            player.changedir('Down')
            
      if event.keysym == 'Right':
            player.changedir('Right')
root.bind("<Key>",kpress)

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
      #creates the snake function
        self.moveblocks.append([0,-10]) #appending 0->-10
        self.snake.append(canvas.create_rectangle(self.x,10*(len(self.snake)+1)+self.y,self.x+10,10*(len(self.snake)+1)+self.y+10,fill='red'))

    def changedir(self,dir1):
        if dir1=='Up':
            self.move = [0,-10] #binding movements to existing WASD values. 
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
        # print(self.move)#checks the x and y coords of the snake
        self.x = self.x + int(self.move[0])
        self.y = self.y + int(self.move[1]) #we readjust the x and y coords
        if self.y < 0 or self.y>500 or self.x<0 or self.x>500:
            sys.exit() #conditiions to crash game
                
    def adjustspeed(self,speed):
        self.speed = speed

    def getspeed(self):
        return self.speed

class powerup:
        xcoord = 0
        ycoord = 0
        id = canvas.create_oval(500,500,500+6,500+6,fill='blue',tag="test")
        #the id of food is a necessary parameter to have as it can be called
  #simply can just create a new oval or new parameter rather than whole new class
        def __init__(self):
            x = random.randrange(30,500,10)
            y = random.randrange(20,500,10) #using random num_gen for food. 
            self.id = canvas.create_oval(x,y+10,x+10,y+20,fill='blue',tag="test")
            self.xcoord=x
            self.ycoord=y
        def move(self):
            x = random.randrange(30,500,10)
            y = random.randrange(20,500,10) #using random num_gen for food.
            canvas.delete("test")
            self.id = canvas.create_oval(x,y+10,x+10,y+20,fill='blue',tag="test")
            self.xcoord=x
            self.ycoord=y

player = Snake(300, 300)
food = powerup()

# button1 = tk.Button(text='Update Speed',command=adjustspeed)
# canvas.create_window(270,18,window=button1)

def tick(player):
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
            time1 = time2
            clock.config(text=time2)
    player.movesnake()
    global food
    if (player.x == food.xcoord) and (player.y == food.ycoord):
          print("Player's pos:",player.x,player.y)
          print("Food Pos: ",food.xcoord,food.ycoord) 
          food.move()
          clock.after(int(100/player.getspeed()),lambda: tick(player))
      
    else:
      clock.after(int(100/player.getspeed()),lambda: tick(player))




input1 = tk.Entry(root)
canvas.create_window(100,20,window=input1)

def adjustspeed():
      x1 = input1.get()
      player.adjustspeed(int(x1))

for i in range(10):
    player.addblock()
tick(player)