from tkinter import *
from tkinter import ttk
from components.scrollable_frame import ScrollableFrame


class GlobalLeaderboard:
    def __init__(self, root, total_score, highest_score):
        self.root = root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.title_label = None
        self.__set_title_label("Global leaderboard")
        self.buttons_frame = ttk.Frame(root, padding="0 0 0 0")
        self.buttons_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.__create_change_order_button("Sort by total score", self.sort_by_total_score)
        self.leaderboard_frame = ttk.Frame(root, padding="0 0 0 0")
        self.leaderboard_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        self.scrollable_frame = ScrollableFrame(self.leaderboard_frame)
        self.total_score_leaderboard = total_score
        self.highest_score_leaderboard = highest_score
        self.clean_leaderboard()
        self.sort_by_highest_score()

    def __create_change_order_button(self, text, command):
        self.change_order_button = Button(self.buttons_frame, text=text, command=command)
        self.change_order_button.grid(column=0, row=0, sticky=(N, W, E, S))

    def __set_title_label(self, text):
        if self.title_label is not None:
            self.title_label.destroy()
        self.title_label = ttk.Label(self.root, text=text)
        self.title_label.grid(column=0, row=0, sticky=W)
        self.title_label.grid_configure(padx=5, pady=5)

    def clean_leaderboard(self):
        for child in self.scrollable_frame.scrollable_frame.winfo_children():
            child.destroy()

    def sort_by_total_score(self):
        self.clean_leaderboard()
        self.change_order_button.destroy()
        self.__create_change_order_button("Sort by highest score", self.sort_by_highest_score)
        self.__set_title_label("Global leaderboard - total score")
        sorted_list = sorted(self.total_score_leaderboard, key=lambda player: player['totalscore'], reverse=True)
        for player in sorted_list:
            ttk.Label(self.scrollable_frame.scrollable_frame,
                      text=f"{player['username']} - {player['totalscore']}").pack()
        self.scrollable_frame.pack()

    def sort_by_highest_score(self):
        self.clean_leaderboard()
        self.change_order_button.destroy()
        self.__create_change_order_button("Sort by total score", self.sort_by_total_score)
        self.__set_title_label("Global leaderboard - highest score")
        print(self.highest_score_leaderboard)
        sorted_list = sorted(self.highest_score_leaderboard, key=lambda player:  player['highestscore'] if 'highestscore' in player else 0, reverse=True)
        for player in sorted_list:
            ttk.Label(self.scrollable_frame.scrollable_frame,
                      text=f"{player['username']} - {player['highestscore']}").pack()
        self.scrollable_frame.pack()
