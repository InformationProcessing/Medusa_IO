from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.global_leaderboard import GlobalLeaderboard
import json
from time import sleep

root = Tk()
root.title("Global leaderboard component testing")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

leaderboard = GlobalLeaderboard(mainframe)

root.mainloop()
#json_obj = json.loads(text)
#print(json_obj['highestscore'])
