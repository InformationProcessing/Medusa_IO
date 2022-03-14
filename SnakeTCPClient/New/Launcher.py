import tkinter as tk
from subprocess import Popen
import os

root = tk.Tk()

def StartC1():
   os.system('python New/SnakeTCPClient1.py')

def StartC2():
   os.system('python New/SnakeTCPClient2.py')

canvas_width = 400
canvas_height = 200
canvas = tk.Canvas(root, width = canvas_width+1, height = canvas_height+1, highlightthickness=10)

canvas.pack()

B1 = tk.Button(root, text = "Launch Client 1", command = StartC1)
canvas.create_window(350,300,window=B1)

B2 = tk.Button(root, text = "Launch Client 2", command = StartC2)
canvas.create_window(350,400,window=B2)


root.mainloop()