from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.global_leaderboard import GlobalLeaderboard


class GameOver:
    def __init__(self, root, username="", score=0):
        self.root = root

        self.game_over_frame = ttk.Frame(root, padding="3 3 12 12")
        self.game_over_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        game_over_label = ttk.Label(self.game_over_frame, text="Game over!")
        game_over_label.grid(column=1, row=1, sticky=(N, W, E))
        game_over_label.grid_configure(padx=5, pady=5)

        username_label = ttk.Label(self.game_over_frame, text=f"Your name: {username}")
        username_label.grid(column=1, row=2, sticky=(N, W, E))
        username_label.grid_configure(padx=5, pady=5)

        score_label = ttk.Label(self.game_over_frame, text=f"Your score: {score}")
        score_label.grid(column=1, row=3, sticky=(N, W, E))
        score_label.grid_configure(padx=5, pady=5)

        self.leader_board_button = Button(root, text="Show global leaderboard",
                                          command=self.__show_global_leader_board)
        self.leader_board_button.grid(column=0, row=2, sticky=(W, E, S))

    def __show_global_leader_board(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        GlobalLeaderboard(self.root)
