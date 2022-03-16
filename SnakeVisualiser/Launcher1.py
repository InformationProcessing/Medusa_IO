import tkinter as tk
from subprocess import Popen
import subprocess
import sys
import os

root = tk.Tk()

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

def StartC1():
   spawn_program_and_die(['python3','New/SnakeTCPClient1.py'])

canvas_width = 400
canvas_height = 200
canvas = tk.Canvas(root, width = canvas_width+1, height = canvas_height+1, highlightthickness=10)

canvas.pack()

B1 = tk.Button(root, text = "Play Again", command = StartC1)
canvas.create_window(200,100,window=B1)

f = open("New/client1.txt","r")

T = tk.Text(root, height=2, width=15)
T.pack()
T.insert(tk.END, f.read())
T.place(x = 145,y = 35)

root.mainloop()