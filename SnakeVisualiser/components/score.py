from tkinter import *
from tkinter import ttk


class Score:
    def __init__(self, root, score=0, scores=None):
        if scores is None:
            scores = []

        self.root = root
        self.score_text = StringVar()
        score_label = ttk.Label(root, textvariable=self.score_text)
        score_label.grid(column=0, row=0, sticky=(N, W))
        score_label.grid_configure(padx=5, pady=5)
        self.score_text.set("Score: " + str(score))
        self.score_frame = ttk.Frame(root, padding="3 3 12 12")
        self.score_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.__create_score_list(scores)

        for child in self.score_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def __create_score_list(self, scores):
        for idx, score in enumerate(scores):
            label = ttk.Label(self.score_frame, text=f"{idx + 1}. {score['player']} - {score['score']}")
            label.grid(column=1, row=idx, sticky=W)
            label.grid_configure(padx=5, pady=5)

    def __clear_score_list(self):
        for widget in self.score_frame.winfo_children():
            widget.destroy()

    def update(self, player_score, player_name, scores):
        self.score_text.set("Score: " + str(player_score))
        player_record = {"player": player_name, "score": player_score}

        inserted = False
        for i in range(0, len(scores)):
            if scores[i]["score"] < player_score:
                scores.insert(i, player_record)
                inserted = True
                break

        if not inserted:
            scores.insert(len(scores), player_record)

        self.__clear_score_list()
        self.__create_score_list(scores)
