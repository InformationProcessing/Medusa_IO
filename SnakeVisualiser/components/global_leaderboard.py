from tkinter import *
from tkinter import ttk
from components.scrollable_frame import ScrollableFrame


class GlobalLeaderboard:
    def __init__(self, root, total_score, highest_score):
        self.root = root
        # root.columnconfigure(1, weight=1)
        # root.rowconfigure(1, weight=1)
        self.style = ttk.Style()
        self.style.configure('TFrame', background='white')
        self.main_frame = ttk.Frame(root, style="TFrame", padding="420 0")
        self.main_frame.grid(row=0, column=0)
        self.logo = PhotoImage(file='SnakeVisualiser/assets/medusaLOGO.png')
        ttk.Label(self.main_frame, image=self.logo, background='white').grid(row=0)

        self.main_frame.grid(row=1, column=0)
        self.title_label = None
        self.__set_title_label("Global leaderboard")

        self.buttons_frame = ttk.Frame(self.root, padding="420 30")
        self.buttons_frame.grid(column=0, row=2, sticky=(N))
        self.__create_change_order_button("Sort by total score", self.sort_by_total_score)

        self.leaderboard_frame = ttk.Frame(self.root, padding="420 0")
        self.leaderboard_frame.grid(column=0, row=3, sticky=(N), pady=20)
        self.scrollable_frame = ScrollableFrame(self.leaderboard_frame)
        self.total_score_leaderboard = total_score
        self.highest_score_leaderboard = highest_score
        self.clean_leaderboard()
        self.sort_by_highest_score()

    def __create_change_order_button(self, text, command):
        self.change_order_button = Button(self.buttons_frame, text=text, command=command, width=20, font=("Arial", 10),
                                          bg="#e91e62", border=2, pady=14)
        self.change_order_button.grid(column=0, row=2, sticky=(N, W, E))
        self.exit_game_button = Button(self.buttons_frame, text="Exit game & close window",
                                            command=self.root.quit, width=20, font=("Arial", 10),
                                          bg="#90caf9", border=2, pady=14)
        self.exit_game_button.grid(column=1, row=2, sticky=(N, W, E))

    def __set_title_label(self, text):
        if self.title_label is not None:
            self.title_label.destroy()
        self.title_label = ttk.Label(self.main_frame, text=text, font=("Arial", 32), background="white")
        self.title_label.grid(column=0, row=1)

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
                      text=f"{player['username']} - {player['totalscore']}", justify="left", background="white").pack()
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
                      text=f"{player['username']} - {player['highestscore']}", justify="left", background="white").pack()
        self.scrollable_frame.pack()
