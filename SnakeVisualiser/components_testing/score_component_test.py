from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.score import Score
from time import sleep

root = Tk()
root.title("Score component testing")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Game column").grid(column=1, row=1, sticky=W)
score_frame = ttk.Frame(mainframe, padding="3 3 12 12")
score_frame.grid(column=2, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

scores = [
    {'player': 'VendaskyCZ1', 'score': 255},
    {'player': 'VendaskyCZ2', 'score': 200},
    {'player': 'VendaskyCZ3', 'score': 0}
]

score = Score(score_frame, 0, scores)


def update_score():
    scores = [
        {'player': 'VendaskyCZ3', 'score': 300},
        {'player': 'VendaskyCZ1', 'score': 255},
        {'player': 'VendaskyCZ2', 'score': 200}
    ]
    score.update(300, scores)


root.after(2000, update_score)
root.mainloop()

sleep(5)
