from tkinter import *
from tkinter import ttk


class GameIntro:
    def __init__(self, root, start_game):
        self.root = root
        self.start_game = start_game

        self.main_frame = ttk.Frame(root, padding=str(0.43 * root.winfo_screenwidth()) + " " + str(
            0.35 * root.winfo_screenheight()))
        self.main_frame.grid(row=0, column=0)
        ttk.Label(self.main_frame, text="Medusa IO", font=("Arial", 32)).grid(row=0)
        self.form_frame = ttk.Frame(self.main_frame)
        self.form_frame.grid(row=1, column=0)

        ttk.Label(self.form_frame, text="Server IP:").grid(row=0)
        ttk.Label(self.form_frame, text="Server port:").grid(row=1)
        ttk.Label(self.form_frame, text="Your port:").grid(row=2)
        ttk.Label(self.form_frame, text="Username:").grid(row=3)

        self.server_ip_entry = ttk.Entry(self.form_frame)
        self.server_port_entry = ttk.Entry(self.form_frame)
        self.client_port_entry = ttk.Entry(self.form_frame)
        self.username_entry = ttk.Entry(self.form_frame)
        self.error_label = None

        self.server_ip_entry.grid(row=0, column=1)
        self.server_port_entry.grid(row=1, column=1)
        self.client_port_entry.grid(row=2, column=1)
        self.username_entry.grid(row=3, column=1)

        def func(event):
            print("You hit return.")
            self.play_button_pressed()

        self.root.bind('<Return>', func)

        self.play_button = Button(self.main_frame, text="Play!", command=self.play_button_pressed, width=10)
        self.play_button.grid(column=0, row=2, sticky=(N, W, E, S))

    def play_button_pressed(self):
        server_ip = self.server_ip_entry.get()
        server_port = int(self.server_port_entry.get())
        client_port = int(self.client_port_entry.get())
        username = self.username_entry.get()
        has_whitespace = False
        for i in username:
            if i == " ": has_whitespace = True

        if self.error_label is not None:
            self.error_label.destroy()

        if username == "":
            self.error_label = ttk.Label(self.main_frame, text="Username cannot be empty!")
            self.error_label.grid(column=0, row=3)
        elif has_whitespace:
            self.error_label = ttk.Label(self.main_frame, text="Username cannot contain whitespace!")
            self.error_label.grid(column=0, row=3)
        else:
            self.start_game(server_ip, server_port, client_port, username)
