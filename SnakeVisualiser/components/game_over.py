from tkinter import *
from tkinter import ttk
from turtle import width
from components.global_leaderboard import GlobalLeaderboard
from components.database_connection import update_score


# TODO: detect that the string is cut and request the new message
def parse_global_leaderboard(database_message):
    split_leaderboards = database_message.split("|")
    leaderboards = []
    try:
        for leaderboard in split_leaderboards:
            new_leaderboard = []
            players_str = leaderboard.split(";")
            for player_str in players_str:
                player_dict = {}
                player_keys_and_vals = player_str.replace("{", "").replace("}", "").split(",")
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
    except:
        print("problem with parsing from the database")
    return leaderboards


# TODO - add local database
class GameOver:
    def __init__(self, root, username="", score=0):
        self.root = root

        self.username = username
        self.score = score
        self.game_over_frame = ttk.Frame(root, padding="300 100")
        self.game_over_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.game_over_frame.grid(row=0, column=0)

        self.main_frame = ttk.Frame(root, padding="360 120 0 0")
        self.main_frame.grid(row=0, column=0)
        self.logo = PhotoImage(file='SnakeVisualiser/assets/medusaLOGO.png')
        ttk.Label(self.main_frame, image=self.logo, background='white').grid(row=0)


        game_over_label = ttk.Label(self.main_frame, text="Game over!", background='white', padding="100 10 5 10", font=("Arial", 12), justify='center')
        game_over_label.grid(column=0, row=1, sticky=(N, W, E))
        game_over_label.grid_configure(padx=5, pady=5)

        username_label = ttk.Label(self.main_frame, text=f"Your name: {username}",background='white', padding="100 10 5 10", font=("Arial", 12), justify='center')
        username_label.grid(column=0, row=2, sticky=(N, W, E))
        username_label.grid_configure(padx=5, pady=5)

        score_label = ttk.Label(self.main_frame, text=f"Your score: {score}",background='white', padding="100 10 5 10", font=("Arial", 12), justify='center')
        score_label.grid(column=0, row=3, sticky=(N, W, E))
        score_label.grid_configure(padx=5, pady=5)

        leaderboards = []
        try:
            received_response = update_score(username, score, 0)
            leaderboards = parse_global_leaderboard(received_response)
        except Exception as err:
            print("Error when fetching from the database: " + str(err))
        self.leaderboard_total_score = []

        if len(leaderboards) > 0:
            for score in leaderboards[0]:
                if 'totalscore' in score:
                    self.leaderboard_total_score.append(score)

        self.leaderboard_highest_score = []
        if len(leaderboards) > 1:
            for score in leaderboards[1]:
                if 'highestscore' in score:
                    self.leaderboard_highest_score.append(score)

        if not len(leaderboards) == 0:
            self.leader_board_button = Button(self.main_frame, text="Show global leaderboard",
                                            command=self.__show_global_leader_board, width=20, font=("Arial", 10),
                                            bg="#e91e62", border=2, pady=14)
            self.leader_board_button.grid(column=0, row=4, sticky=(N, S), pady=10)
        self.exit_game_button = Button(self.main_frame, text="Exit game & close window", font=("Arial", 10),
                                            command=self.root.quit, bg="#90caf9", border=2, pady=10, padx=10, width=22)
        self.exit_game_button.grid(column=1, row=4, sticky=( E, S))

    def __show_global_leader_board(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        GlobalLeaderboard(self.root, self.leaderboard_total_score, self.leaderboard_highest_score)

    def get_player_position(self):
        if hasattr(self, 'leaderboard_highest_score'):
            for x in range(0, len(self.leaderboard_highest_score)):
                leaderboard_record = self.leaderboard_highest_score[x]
                if 'username' in leaderboard_record:
                    if leaderboard_record['username'] == self.username:
                        return x + 1
            return len(self.leaderboard_highest_score)
        return 1
