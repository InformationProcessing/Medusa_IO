from tkinter import *
from tkinter import ttk


class GameIntro:
    def __init__(self, root, start_game):
        self.root = root
        self.start_game = start_game
        self.style = ttk.Style()
        self.style.configure('TFrame', background='white')

        self.main_frame = ttk.Frame(root, padding=str(0.27 * root.winfo_screenwidth()) + " "
                                                 + str(0.1 * root.winfo_screenheight()), style="TFrame")

        self.main_frame.grid(row=0, column=0)
        self.logo = PhotoImage(file='SnakeVisualiser/assets/medusaLOGO.png')
        ttk.Label(self.main_frame, image=self.logo, background='white').grid(row=0)

        self.form_frame = ttk.Frame(self.main_frame, padding="0 0 0 30")
        self.form_frame.grid(row=1, column=0)

        ttk.Label(self.form_frame, text="Server IP", background='white', padding="0 10 5 10", font=("Arial", 12), justify='left').grid(row=0)
        ttk.Label(self.form_frame, text="Server port", background='white', padding="0 10 5 10", font=("Arial", 12), justify='left').grid(row=1)
        ttk.Label(self.form_frame, text="Your port", background='white', padding="0 10 5 10", font=("Arial", 12), justify='left').grid(row=2)
        ttk.Label(self.form_frame, text="Username", background='white', padding="0 10 5 10", font=("Arial", 12), justify='left').grid(row=3)

        self.server_ip_entry = ttk.Entry(self.form_frame, font=("Arial", 12))
        self.server_port_entry = ttk.Entry(self.form_frame, font=("Arial", 12))
        self.client_port_entry = ttk.Entry(self.form_frame, font=("Arial", 12))
        self.username_entry = ttk.Entry(self.form_frame, font=("Arial", 12))
        self.error_label = None

        self.server_ip_entry.grid(row=0, column=1)
        self.server_port_entry.grid(row=1, column=1)
        self.client_port_entry.grid(row=2, column=1)
        self.username_entry.grid(row=3, column=1)

        def func(event):
            print("You hit return.")
            self.play_button_pressed()

        self.root.bind('<Return>', func)

        self.play_button = Button(self.main_frame, text="Play!",font=("Arial", 14), command=self.play_button_pressed, 
                                width=10, pady=10, bg="#e91e62", border=2)
        self.play_button.grid(column=0, row=3, sticky=(N, S), pady=10)
        self.exit_game_button = Button(self.main_frame, text="Exit game & close window",
                                         font=("Arial", 10), command=self.root.quit,  bg="#90caf9",
                                         border=2, pady=10)
        self.exit_game_button.grid(column=1, row=4, sticky=(E, S))

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
            self.error_label = ttk.Label(self.main_frame, text="Username cannot be empty!", background='white', padding="0 10 5 10", font=("Arial", 10))
            self.error_label.grid(column=0, row=4)
        elif has_whitespace:
            self.error_label = ttk.Label(self.main_frame, text="Username cannot contain whitespace!", background='white', padding="0 10 5 10", font=("Arial", 10))
            self.error_label.grid(column=0, row=4)
        else:
            self.start_game(server_ip, server_port, client_port, username)
