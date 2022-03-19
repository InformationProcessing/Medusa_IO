from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.global_leaderboard import GlobalLeaderboard
from SnakeVisualiser.components.database_connection import update_score


#TODO: detect that the string is cut and request the new message
def parse_global_leaderboard(database_message):
    split_leaderboards = database_message.split("|")
    leaderboards = []
    for leaderboard in split_leaderboards:
        new_leaderboard = []
        players_str = leaderboard.split(";")
        for player_str in players_str:
            player_dict = {}
            player_keys_and_vals = player_str.replace("{","").replace("}", "").split(",")
            for key_val_str in player_keys_and_vals:
                key_val_array = key_val_str.split(":")
                if len(key_val_array) > 1:
                    key = key_val_array[0].strip().replace("'", "")
                    value_str = key_val_array[1].strip().replace("'", "")
                    if "Decimal(" in value_str:
                        player_dict[key] = int(value_str.replace("Decimal(", "").replace(")", ""))
                    else:
                        player_dict[key] = value_str.strip().replace("'", "")
            new_leaderboard.append(player_dict)
        leaderboards.append(new_leaderboard)
    return leaderboards


# TODO - add local database
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

        received_response = update_score(username, score, 0)
        leaderboards = parse_global_leaderboard(received_response)
        self.leaderboard_total_score = []
        for score in leaderboards[0]:
            if 'totalscore' in score:
                self.leaderboard_total_score.append(score)

        self.leaderboard_highest_score = []
        for score in leaderboards[1]:
            if 'highestscore' in score:
                self.leaderboard_highest_score.append(score)

        self.leader_board_button = Button(root, text="Show global leaderboard",
                                          command=self.__show_global_leader_board)
        self.leader_board_button.grid(column=0, row=2, sticky=(W, E, S))

    def __show_global_leader_board(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        GlobalLeaderboard(self.root, self.leaderboard_total_score, self.leaderboard_highest_score)
