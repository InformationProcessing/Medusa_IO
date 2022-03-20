import tkinter as tk
from tkinter import ttk
from tkinter import *
from components.score import Score
from components.game_over import GameOver
import time
import sys
import random
import os

root = None
mainframe = None
score_board = None
canvas = None
player = None
sharedFood = None
localFood = None

clock = None
food = None
bg = None
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700
DEFAULT_SNAKE_LENGTH = 10


class Snake:
    snake = []
    snakeblockscoordX = []
    snakeblockscoordY = []
    snakeShadow = []
    snakeblockscoordXShadow = []
    snakeblockscoordYShadow = []
    shadowCreated = False
    x_s = 0
    y_s = 0

    x = 0
    y = 0
    move = [0, 10]
    moveblocks = []
    speed = 1

    def __init__(self, xcord, ycord):
        self.x = xcord
        self.y = ycord
        for i in range(10):
            self.initaddblock(i)

    def initaddblock(self, i):
        self.moveblocks.append([0, 0])
        block = tk.Canvas(canvas, width=10, height=10, bd=0, highlightthickness=0.5, highlightbackground="#870083",
                          relief='ridge', bg="#FF00B7")
        block.place(x=710, y=710)
        self.snake.append(block)
        self.snakeblockscoordX.append(self.x)
        self.snakeblockscoordY.append(self.y - i * 10)

    def addblock(self, i):
        for x in range(0, i):
            self.moveblocks.append([0, 0])
            x_coords = [self.snakeblockscoordX[len(self.snakeblockscoordX) - 2],
                        self.snakeblockscoordX[len(self.snakeblockscoordX) - 1]]
            y_coords = [self.snakeblockscoordY[len(self.snakeblockscoordY) - 2],
                        self.snakeblockscoordY[len(self.snakeblockscoordY) - 1]]
            new_x_cord = x_coords[1]
            new_y_cord = y_coords[1]
            if x_coords[0] == x_coords[1]:
                if y_coords[0] < y_coords[1]:
                    new_y_cord = y_coords[1] + 10
                else:
                    new_y_cord = y_coords[1] - 10
            else:
                if x_coords[0] < x_coords[1]:
                    new_x_cord = x_coords[1] + 10
                else:
                    new_x_cord = x_coords[1] - 10

            if new_y_cord < 0:
                new_y_cord += 710
            if new_x_cord < 0:
                new_x_cord += 710

            block = tk.Canvas(canvas, width=10, height=10, bd=0, highlightthickness=0.5, highlightbackground="#870083",
                              relief='ridge', bg="#FF00B7")
            block.place(x=new_x_cord, y=new_y_cord)
            self.snake.append(block)
            self.snakeblockscoordX.append(new_x_cord)
            self.snakeblockscoordY.append(new_y_cord)
        # print("initialise: ", i, "----",self.snakeblockscoordX[i], "- ",self.snakeblockscoordY[i])

    def widen(self):
        temp = len(self.snake)
        # for i in range(temp):
        #     self.snakeblockscoordX.append(self.snakeblockscoordX[i]+10)
        #     self.snakeblockscoordYShadow.append(self.snakeblockscoordYShadow[i]+10)

        #     block=tk.Canvas(canvas,width=10, height=10, bd=0, highlightthickness=0.5, highlightbackground="white", relief='ridge', bg="yellow")
        #     block.place(x=self.snakeblockscoordX[i]+10, y=self.snakeblockscoordYShadow[i]+10)
        #     self.snake.append(block)
        if self.shadowCreated == False:
            for i in range(temp):
                block = tk.Canvas(canvas, width=10, height=10, bd=0, highlightthickness=0.5,
                                  highlightbackground="#870083", relief='ridge', bg="white")
                block.place(x=self.snakeblockscoordX[i], y=self.snakeblockscoordY[i] + 10)
                self.snakeShadow.append(block)
                self.snakeblockscoordXShadow.append(self.snakeblockscoordX[i] + 10)
                self.snakeblockscoordYShadow.append(self.snakeblockscoordY[i] + 10)
                print("initialise: ", i, "----", self.snakeblockscoordXShadow[i], "- ", self.snakeblockscoordYShadow[i])
        self.x_s = self.x
        self.y_s = self.y
        self.shadowCreated = True

    def changedir(self, dir1):
        if dir1 == 'Up':
            self.move = [0, -10]
        elif dir1 == 'Left':
            self.move = [-10, 0]
        elif dir1 == 'Down':
            self.move = [0, 10]
        elif dir1 == 'Right':
            self.move = [10, 0]

    def movesnake(self):
        # special teleportation of a block
        def abs_move(new_x, new_y, j):
            self.snake[j].place(x=new_x, y=new_y)
            self.snakeblockscoordX[j] = new_x
            self.snakeblockscoordY[j] = new_y
            self.x = self.snakeblockscoordX[0]
            self.y = self.snakeblockscoordY[0]

        # passing on block movement orientation.step to the following block
        for j in range(len(self.moveblocks) - 1, 0, -1):
            self.moveblocks[j] = self.moveblocks[j - 1]
            self.snakeblockscoordX[j] = self.snakeblockscoordX[j - 1]
            self.snakeblockscoordY[j] = self.snakeblockscoordY[j - 1]
            # print("pos:", j, "----",self.snakeblockscoordX[j], ": ",self.snakeblockscoordY[j])
        self.moveblocks[0] = self.move
        # blocking moving backwards and overlapping snake
        if self.moveblocks[0][0] == -self.moveblocks[1][0]:
            self.moveblocks[0][0] = self.moveblocks[1][0]
        if self.moveblocks[0][1] == -self.moveblocks[1][1]:
            self.moveblocks[0][1] = self.moveblocks[1][1]

        # print(self.x, " ", self.y)
        # for every block in the snake, move or teleport
        for j in range(len(self.snake)):
            if self.snakeblockscoordX[j] < 10 or self.snakeblockscoordX[j] > CANVAS_WIDTH or self.snakeblockscoordY[
                j] < 10 or self.snakeblockscoordY[j] > CANVAS_HEIGHT:
                if self.snakeblockscoordX[j] < 10:             abs_move(CANVAS_WIDTH, self.snakeblockscoordY[j], j)
                if self.snakeblockscoordX[j] > CANVAS_WIDTH:   abs_move(10, self.snakeblockscoordY[j], j)
                if self.snakeblockscoordY[j] < 10:             abs_move(self.snakeblockscoordX[j], CANVAS_HEIGHT, j)
                if self.snakeblockscoordY[j] > CANVAS_HEIGHT:  abs_move(self.snakeblockscoordX[j], 10, j)
            else:
                # print(j, "----",self.moveblocks[j][0], "- ",self.moveblocks[j][1])
                self.snake[j].place(x=self.snakeblockscoordX[j], y=self.snakeblockscoordY[j])

        self.x = self.x + int(self.moveblocks[0][0])
        self.y = self.y + int(self.moveblocks[0][1])
        self.snakeblockscoordX[0] = self.x
        self.snakeblockscoordY[0] = self.y

    def teleport(self, new_x, new_y, j):
        self.snake[j].place(x=new_x, y=new_y)
        self.snakeblockscoordX[j] = new_x
        self.snakeblockscoordY[j] = new_y
        self.x = self.snakeblockscoordX[0]
        self.y = self.snakeblockscoordY[0]
        self.movesnake()

    def moveShadow(self):
        # special teleportation of a block
        def abs_move(new_x, new_y, j):
            self.snakeShadow[j].place(x=new_x, y=new_y)
            self.snakeblockscoordXShadow[j] = new_x
            self.snakeblockscoordYShadow[j] = new_y
            self.x_s = self.snakeblockscoordXShadow[0]
            self.y_s = self.snakeblockscoordYShadow[0]

        # passing on block movement orientation.step to the following block
        for j in range(len(self.snakeShadow) - 1, 0, -1):
            # self.moveblocks[j]=self.moveblocks[j-1]
            self.snakeblockscoordXShadow[j] = self.snakeblockscoordXShadow[j - 1]
            self.snakeblockscoordYShadow[j] = self.snakeblockscoordYShadow[j - 1]
            # print("pos:", j, "----",self.snakeblockscoordXShadow[j], ": ",self.snakeblockscoordYShadow[j])
        # self.moveblocks[0]=self.move
        # blocking moving backwards and overlapping snakeShadow
        # if self.moveblocks[0][0] == -self.moveblocks[1][0]:
        #     self.moveblocks[0][0] = self.moveblocks[1][0]
        # if self.moveblocks[0][1] == -self.moveblocks[1][1]:
        #     self.moveblocks[0][1] = self.moveblocks[1][1]

        # print(self.x, " ", self.y)
        # for every block in the snakeShadow, move or teleport
        for j in range(len(self.snakeShadow)):
            if self.snakeblockscoordXShadow[j] < 10 or self.snakeblockscoordXShadow[j] > CANVAS_WIDTH or \
                    self.snakeblockscoordYShadow[j] < 10 or self.snakeblockscoordYShadow[j] > CANVAS_HEIGHT:
                if self.snakeblockscoordXShadow[j] < 10:             abs_move(CANVAS_WIDTH,
                                                                              self.snakeblockscoordYShadow[j], j)
                if self.snakeblockscoordXShadow[j] > CANVAS_WIDTH:   abs_move(10, self.snakeblockscoordYShadow[j], j)
                if self.snakeblockscoordYShadow[j] < 10:             abs_move(self.snakeblockscoordXShadow[j],
                                                                              CANVAS_HEIGHT, j)
                if self.snakeblockscoordYShadow[j] > CANVAS_HEIGHT:  abs_move(self.snakeblockscoordXShadow[j], 10, j)
            else:
                # print(j, "----",self.moveblocks[j][0], "- ",self.moveblocks[j][1])
                self.snakeShadow[j].place(x=self.snakeblockscoordXShadow[j], y=self.snakeblockscoordYShadow[j])

        self.x_s = self.x_s + int(self.moveblocks[0][0])
        self.y_s = self.y_s + int(self.moveblocks[0][1])
        self.snakeblockscoordXShadow[0] = self.x_s
        self.snakeblockscoordYShadow[0] = self.y_s
        print(self.x_s, "   ", self.y_s)

    def teleportShadow(self, new_x, new_y, j):
        self.snakeShadow[j].place(x=new_x, y=new_y)
        self.snakeblockscoordXShadow[j] = new_x
        self.snakeblockscoordYShadow[j] = new_y
        self.x_s = self.snakeblockscoordXShadow[0]
        self.y_s = self.snakeblockscoordYShadow[0]
        self.moveShadow()

    def deleteShadow(self):
        for i in range(len(self.snakeShadow)):
            canvas.delete(self.snakeShadow[i])

    def adjustspeed(self, speed):
        self.speed = speed

    def getspeed(self):
        return self.speed

    def calculate_score(self):
        return len(self.moveblocks) - DEFAULT_SNAKE_LENGTH


def snakeAnnimation(p, animation):
    if animation == "grow":
        for j in range(len(p.snake)):
            if j%2==0: p.snake[j].configure(bg="#90caf9")
            else: p.snake[j].configure(bg="#e91e62")
    elif animation == "ultra_speed":
        for j in range(len(p.snake)):
            p.snake[j].configure(bg="#FFAC00")
    elif animation == "slow_down":
        for j in range(len(p.snake)):
            p.snake[j].configure(bg="#9D67FF")
    elif animation == "shadow":
        for j in range(len(p.snake)):
            if j % 2 == 0:
                p.snake[j].configure(bg="grey")
            else:
                p.snake[j].configure(bg="white")
    elif animation == "return":
        for j in range(len(p.snake)):
            p.snake[j].configure(bg="#FF00B7")

class powerup:
    power_ups = []
    power_upsX = []
    power_upsY = []
    # foodTypes = ["grow", "portal", "ultra_speed","slow_down"]
    # colours = ["red", "blue", "orange", "green"]
    # powerTypes = [["grow","#FF0000"] , ["portal", "#73FF00"] , ["ultra_speed", "#FFAC00"] , ["slow_down", "#9D67FF"], ["shadow", "white"]]
    powerTypes = [["grow", "#FF0000"], ["portal", "#73FF00"], ["ultra_speed", "#FFAC00"], ["slow_down", "#9D67FF"]]
    # powerTypes = [["shadow", "white"]]
    radius = 10
    j = 1

    tagval = ["test0"]

    def __init__(self):
        x = random.randrange(30, 500, 10)
        y = random.randrange(30, 500, 10)  # using random num_gen for food.
        powerRandom = ["grow", "#FF0000"]
        id = canvas.create_oval(x, y, x + self.radius, y + self.radius, fill=powerRandom[1], tag="test0")
        self.power_ups.append([id, powerRandom[0]])
        self.power_upsX.append(x)
        self.power_upsY.append(y)
        # self.tagval.append("test0")

    def generate(self):
        for s in range(random.choice([1, 2])):
            x = random.randrange(30, 500, 10)
            y = random.randrange(20, 500, 10)
            powerRandom = random.choice(self.powerTypes)
            id = canvas.create_oval(x, y, x + self.radius, y + self.radius, fill=powerRandom[1],
                                    tag="test" + str(self.j))
            self.tagval.append("test" + str(self.j))
            self.power_ups.append([id, powerRandom[0]])
            self.power_upsX.append(x)
            self.power_upsY.append(y)
            self.j = self.j + 1

    def delete(self, j):
        self.power_ups.pop(j)
        self.power_upsX.pop(j)
        self.power_upsY.pop(j)
        canvas.delete(self.tagval.pop(j))
        print("Deleted")

    def powerupType(self, p, type):
        # if p.shadowCreated == True:
        #     for j in range(len(p.snakeShadow)):
        #         p.teleportShadow(1000,1000,j)
        #     p.shadowCreated = False
        if type == "portal":
            new_x = random.randrange(30, 500, 10)
            new_y = random.randrange(20, 500, 10)
            p.adjustspeed(1)
            for j in range(len(p.snake)):
                p.teleport(new_x, new_y, j)
                new_x = new_x - 10
        elif type == "grow":
            p.addblock(1)
            p.adjustspeed(1)
            p.shadowCreated = False
            snakeAnnimation(p, "grow")
            clock.after(int(200 / player.getspeed()), lambda: snakeAnnimation(player, "return"))
        elif type == "ultra_speed":
            p.adjustspeed(2)
            p.shadowCreated = False
            snakeAnnimation(p, "ultra_speed")
            clock.after(int(200 / player.getspeed()), lambda: snakeAnnimation(player, "return"))
        elif type == "slow_down":
            p.adjustspeed(0.5)
            p.shadowCreated = False
            snakeAnnimation(p, "slow_down")
            clock.after(int(200 / player.getspeed()), lambda: snakeAnnimation(player, "return"))
        elif type == "shadow":
            p.widen()
            snakeAnnimation(p, "shadow")
            clock.after(int(200 / player.getspeed()), lambda: snakeAnnimation(player, "return"))

class SharedPowerup:
    shared_power_upX = 0
    shared_power_upY = 0
    # foodTypes = ["grow", "portal", "ultra_speed","slow_down"]
    # colours = ["red", "blue", "orange", "green"]
    radius = 30
    tagval = "shared0"

    def __init__(self):
        x = 200
        y = 200  # using random num_gen for food.
        power = [["Ultra-Power", "#FFAC00"]]
        id = canvas.create_oval(x, y, x + self.radius, y + self.radius, fill="#FFAC00", tag="shared0")
        self.shared_power_upX = x
        self.shared_power_upY = y

    def generateShared(self, _x, _y):
        print("Generated")
        x = _x
        y = _y
        power = [["Ultra-Power", "#FFAC00"]]
        id = canvas.create_oval(x, y, x + self.radius, y + self.radius, fill="#FFAC00", tag="shared0")
        self.shared_power_upX = x
        self.shared_power_upY = y

    def deleteShared(self):
        self.shared_power_upX = 0
        self.shared_power_upY = 0
        canvas.delete(self.tagval)
        print("Deleted")

    def powerupType(self, p, type):
        if type == "Ultra-Power":
            p.adjustspeed(1)
            print("should add 5 foods")
            p.addblock(5)
            p.shadowCreated = False
            snakeAnnimation(p, "grow")
            clock.after(int(200 / player.getspeed()), lambda: snakeAnnimation(player, "return"))


allplayers = []


def kpress(event):
    if event.keysym == 'Up':
        player.changedir('Up')

    if event.keysym == 'Left':
        player.changedir('Left')

    if event.keysym == 'Down':
        player.changedir('Down')

    if event.keysym == 'Right':
        player.changedir('Right')


def show_game_over(username, score):
    for widget in mainframe.winfo_children():
        widget.destroy()

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    game_over_frame = ttk.Frame(mainframe, padding="3 3 12 12")
    game_over_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    game_over_widget = GameOver(game_over_frame, username, score)
    return game_over_widget.get_player_position()


def update_score(player_score, player_name, scores):
    score_board.update(player_score, player_name, scores)


def init_game():
    global mainframe, score_board, canvas, clock, player, food, bg, sharedFood, localFood
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    score_frame = ttk.Frame(mainframe, padding="3 3 12 12")
    score_frame.grid(column=1, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    score_board = Score(score_frame, 0, [])

    time1 = ''
    clock = Label(root)

    game_frame = ttk.Frame(mainframe, padding="180 60 12 12")
    game_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    canvas = tk.Canvas(game_frame, width=CANVAS_WIDTH + 1, height=CANVAS_HEIGHT + 1, highlightthickness=10,
                       highlightbackground="black")
    bg = PhotoImage(file="SnakeVisualiser/assets/map4.png")
    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.pack()

    player = Snake((random.randint(100, 700) // 10) * 10, (random.randint(100, 700) // 10) * 10)
    allplayers.append(player)
    sharedFood = SharedPowerup()
    localFood = powerup()
    # snakeShadow = Snake((random.randint(100,700)//10)*10,(random.randint(100,700)//10)*10)
