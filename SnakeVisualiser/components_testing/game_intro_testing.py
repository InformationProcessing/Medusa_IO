from tkinter import *
from tkinter import ttk
from SnakeVisualiser.components.game_intro import GameIntro


def start_game(server_ip, server_port, client_port, username):
    print("Starting game with server IP: " + server_ip + ", server port: " + server_port + ", client port: " + client_port + ", username: " + username)


root = Tk()
root.title("Game intro component testing")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

leaderboard = GameIntro(mainframe, start_game)

root.mainloop()
