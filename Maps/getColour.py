import tkinter as tk
from PIL import ImageGrab
# https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html#PIL.ImageGrab.grab

master = tk.Tk()
master.columnconfigure(0, weight = 1)
master.title("Colors")

button = tk.Button(master, text = "Press Spacebar")
button.grid(sticky = tk.NSEW)

canvas = tk.Canvas(master, width = 200, height = 200)
canvas.grid(sticky = tk.NSEW)

pic = ImageGrab.grab()

def color():
    x, y = master.winfo_pointerx(), master.winfo_pointery()
    r, g, b = pic.getpixel((x, y))
    hue = f"#{r:02x}{g:02x}{b:02x}"
    button.config( text = f"{x}, {y} =  {hue}")
    canvas["background"] = hue

button["command"] = color
button.focus_force()

master.mainloop()
