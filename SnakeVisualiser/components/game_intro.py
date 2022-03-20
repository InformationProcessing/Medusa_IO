from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class GameIntro:
    def __init__(self, root, start_game):
        self.root = root
        self.start_game = start_game

        self.main_frame = ttk.Frame(root, padding=str(0.43*root.winfo_screenwidth())+" "+str(0.35*root.winfo_screenheight()))
        self.main_frame.grid(row=0, column=0)
        ttk.Label(self.main_frame, text="Medusa IO", font=("Arial",30)).grid(row=0)
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
        # server_ip = "localhost"
        # server_port = 12000
        # client_port = 13000
        # username = "c"
        haswhitespace = False
        for i in username:
            if i == " ": haswhitespace = True
            
        if (haswhitespace) or username == "":
            ttk.Label(self.form_frame, text="Username needed or wrong format given!").grid(row=4)
            username = self.username_entry.get()
        else:
            self.start_game(server_ip, server_port, client_port, username)
# from tkinter import *
# from tkinter import ttk

# class GameIntro:
#     def __init__(self, root, start_game):
#         window = Tk()
#         # set window title
#         window.title("Python GUI App")
#         # set window width and height
#         window.configure(width=500, height=300)
#         # set window background color
#         window.configure(bg='lightgray')
#         self.root = root
#         root.eval('tk::PlaceWindow . center')
#         self.start_game = start_game
#         screen_width = str(root.winfo_screenwidth())
#         screen_height = str(root.winfo_screen())
#         self.main_frame = ttk.Frame(root, height=121, width=3456)
#         self.main_frame.grid(row=0, column=0)
#         ttk.Label(self.main_frame, text="Medusa IO").grid(row=0)
#         self.form_frame = ttk.Frame(self.main_frame)
#         self.form_frame.grid(row=1, column=0)

#         ttk.Label(self.form_frame, text="Server IP:").grid(row=0)
#         ttk.Label(self.form_frame, text="Server port:").grid(row=1)
#         ttk.Label(self.form_frame, text="Your port:").grid(row=2)
#         ttk.Label(self.form_frame, text="Username:").grid(row=3)

#         self.server_ip_entry = ttk.Entry(self.form_frame)
#         self.server_port_entry = ttk.Entry(self.form_frame)
#         self.client_port_entry = ttk.Entry(self.form_frame)
#         self.username_entry = ttk.Entry(self.form_frame)

#         self.server_ip_entry.grid(row=0, column=1)
#         self.server_port_entry.grid(row=1, column=1)
#         self.client_port_entry.grid(row=2, column=1)
#         self.username_entry.grid(row=3, column=1)

#         self.play_button = Button(self.main_frame, text="Play!", command=self.play_button_pressed)
#         self.play_button.grid(column=0, row=2, sticky=(N, W, E, S))

#     def play_button_pressed(self):
#         server_ip = self.server_ip_entry.get()
#         server_port = int(self.server_port_entry.get())
#         client_port = int(self.client_port_entry.get())
#         username = self.username_entry.get()
#         self.start_game(server_ip, server_port, client_port, username)
        
