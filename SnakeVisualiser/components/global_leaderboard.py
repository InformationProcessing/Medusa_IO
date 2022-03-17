from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.scrollable_frame import ScrollableFrame


class GlobalLeaderboard:
    def __init__(self, root):
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
        self.fetched_players = self.__fetch_players()
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

    def __fetch_players(self):
        return [
            {'highestscore': 400, 'username': 'ccl', 'totalscore': 1131, 'other_key': 'a75', 'kills': 404},
            {'highestscore': 401, 'username': 'abc', 'totalscore': 2121, 'other_key': 'aa75', 'kills': 400},
            {'highestscore': 403, 'username': 'edf', 'totalscore': 2221, 'other_key': 'aa75', 'kills': 405},
            {'highestscore': 203, 'username': 'ghj', 'totalscore': 2521, 'other_key': 'aa75', 'kills': 505},
            {'highestscore': 303, 'username': 'cdf', 'totalscore': 1521, 'other_key': 'aa75', 'kills': 305},
            {'highestscore': 203, 'username': 'acdf', 'totalscore': 1421, 'other_key': 'aa65', 'kills': 205},
            {'highestscore': 1203, 'username': 'VendaskyCZ', 'totalscore': 14210, 'other_key': 'aa65',
             'kills': 2050},
            {'highestscore': 400, 'username': 'ccl', 'totalscore': 1131, 'other_key': 'a75', 'kills': 404},
            {'highestscore': 401, 'username': 'abc', 'totalscore': 2121, 'other_key': 'aa75', 'kills': 400},
            {'highestscore': 403, 'username': 'edf', 'totalscore': 2221, 'other_key': 'aa75', 'kills': 405},
            {'highestscore': 203, 'username': 'ghj', 'totalscore': 2521, 'other_key': 'aa75', 'kills': 505},
            {'highestscore': 303, 'username': 'cdf', 'totalscore': 1521, 'other_key': 'aa75', 'kills': 305},
            {'highestscore': 203, 'username': 'acdf', 'totalscore': 1421, 'other_key': 'aa65', 'kills': 205},
            {'highestscore': 1203, 'username': 'VendaskyCZ', 'totalscore': 14210, 'other_key': 'aa65',
             'kills': 2050},
            {'highestscore': 400, 'username': 'ccl', 'totalscore': 1131, 'other_key': 'a75', 'kills': 404},
            {'highestscore': 401, 'username': 'abc', 'totalscore': 2121, 'other_key': 'aa75', 'kills': 400},
            {'highestscore': 403, 'username': 'edf', 'totalscore': 2221, 'other_key': 'aa75', 'kills': 405},
            {'highestscore': 203, 'username': 'ghj', 'totalscore': 2521, 'other_key': 'aa75', 'kills': 505},
            {'highestscore': 303, 'username': 'cdf', 'totalscore': 1521, 'other_key': 'aa75', 'kills': 305},
            {'highestscore': 203, 'username': 'acdf', 'totalscore': 1421, 'other_key': 'aa65', 'kills': 205},
            {'highestscore': 1203, 'username': 'VendaskyCZ', 'totalscore': 14210, 'other_key': 'aa65',
             'kills': 2050},
            {'highestscore': 400, 'username': 'ccl', 'totalscore': 1131, 'other_key': 'a75', 'kills': 404},
            {'highestscore': 401, 'username': 'abc', 'totalscore': 2121, 'other_key': 'aa75', 'kills': 400},
            {'highestscore': 403, 'username': 'edf', 'totalscore': 2221, 'other_key': 'aa75', 'kills': 405},
            {'highestscore': 203, 'username': 'ghj', 'totalscore': 2521, 'other_key': 'aa75', 'kills': 505},
            {'highestscore': 303, 'username': 'cdf', 'totalscore': 1521, 'other_key': 'aa75', 'kills': 305},
            {'highestscore': 203, 'username': 'acdf', 'totalscore': 1421, 'other_key': 'aa65', 'kills': 205},
            {'highestscore': 1203, 'username': 'VendaskyCZ', 'totalscore': 14210, 'other_key': 'aa65',
             'kills': 2050},
            {'highestscore': 400, 'username': 'ccl', 'totalscore': 1131, 'other_key': 'a75', 'kills': 404},
            {'highestscore': 401, 'username': 'abc', 'totalscore': 2121, 'other_key': 'aa75', 'kills': 400},
            {'highestscore': 403, 'username': 'edf', 'totalscore': 2221, 'other_key': 'aa75', 'kills': 405},
            {'highestscore': 203, 'username': 'ghj', 'totalscore': 2521, 'other_key': 'aa75', 'kills': 505},
            {'highestscore': 303, 'username': 'cdf', 'totalscore': 1521, 'other_key': 'aa75', 'kills': 305},
            {'highestscore': 203, 'username': 'acdf', 'totalscore': 1421, 'other_key': 'aa65', 'kills': 205},
            {'highestscore': 1203, 'username': 'VendaskyCZ', 'totalscore': 14210, 'other_key': 'aa65',
             'kills': 2050},
        ]

    def clean_leaderboard(self):
        for child in self.scrollable_frame.scrollable_frame.winfo_children():
            child.destroy()

    def sort_by_total_score(self):
        self.clean_leaderboard()
        self.change_order_button.destroy()
        self.__create_change_order_button("Sort by highest score", self.sort_by_highest_score)
        self.__set_title_label("Global leaderboard - total score")
        sorted_list = sorted(self.fetched_players, key=lambda player: player['totalscore'], reverse=True)
        for player in sorted_list:
            ttk.Label(self.scrollable_frame.scrollable_frame,
                      text=f"{player['username']} - {player['totalscore']}").pack()
        self.scrollable_frame.pack()

    def sort_by_highest_score(self):
        self.clean_leaderboard()
        self.change_order_button.destroy()
        self.__create_change_order_button("Sort by total score", self.sort_by_total_score)
        self.__set_title_label("Global leaderboard - highest score")
        sorted_list = sorted(self.fetched_players, key=lambda player: player['highestscore'], reverse=True)
        for player in sorted_list:
            ttk.Label(self.scrollable_frame.scrollable_frame,
                      text=f"{player['username']} - {player['highestscore']}").pack()
        self.scrollable_frame.pack()
