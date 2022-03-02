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

server_port = 12001
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
welcome_socket.bind(('',server_port))

c1add = ('localhost',13000)
c2add = ('localhost',14000)

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
msg1 = ""
msg2 = ""

while 1:
    time2 = time.strftime('%H:%M:%S')
    deleteblocks()
    
    cmsg, cadd = welcome_socket.recvfrom(2048)  	
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        print("1",cmsg)
        msg1 = cmsg
        welcome_socket.sendto(msg1.encode(), c2add)
    else:
        print("2",cmsg)
        msg2 = cmsg
        welcome_socket.sendto(msg2.encode(), c1add)
    
    print(cmsg)
    
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
            
    updateothers()