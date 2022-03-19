import tkinter as tk
from tkinter import *
import time
import sys
import random
import os
import socket
import subprocess
import sys
import atexit
import components.SnakeGameMap as SnakeGameMap
from components.game_intro import GameIntro
from components.fpga_communicator import FPGACommunicator

root = tk.Tk()
fpga_communicator = FPGACommunicator()

client_port = None
server_ip = None
server_port = None
username = None
player = None
food = None
wefoundfood = 0
_x = 0
_y = 0
_r = 0
_j = 0

time1 = ''
clock = None
game_over = False

otherplayer = []
otherplayerblocks = []


def exit_handler():
    msg = "0,0;|0,0,0,0,0"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('', client_port))
    client_socket.sendto(msg.encode(), (server_ip, server_port))


atexit.register(exit_handler)


def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)


def mergearray(array1, array2):
    newarray = []
    for i in range(len(array1)):
        newarray.append([array1[i] + 100, array2[i] + 100])
    return newarray



def calculate_score_table(other_players, client_name):
    score_table = []

    for other_player in other_players:
        score = len(other_player["blocks"].split(";"))
        score_table.append({"player": other_player["name"], "score": score})

    return score_table


def sendCoord():
    global client_port, wefoundfood, server_port, game_over
    msg = username + "|"
    for i in range(len(player.snakeblockscoordX)):
        msg += str(player.snakeblockscoordX[i]) + "," + str(player.snakeblockscoordY[i]) + ";"
    msg = msg + "|" + str(_x) + "," + str(_y) + "," + str(_r) + "," + str(_j) + "," + str(wefoundfood)
    wefoundfood = 0
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('', client_port))
    client_socket.sendto(msg.encode(), (server_ip, server_port))
    msg, sadd = client_socket.recvfrom(2048)

    if msg.decode() == "dead":
        game_over = True
        return []

    users = msg.decode().split("\n")
    snakes = []
    foodinfo = []

    for i in range(len(users)):
        if len(users[i].split('|')) > 1:
            snakes.append({'name': users[i].split('|')[0], 'blocks': users[i].split('|')[1]})
            foodinfo.append(users[i].split('|')[2])

    for i in range(len(foodinfo)):
        tempfood = foodinfo[i].split(",")
        if tempfood[4] == '1':
            global food
            food.delete(int(tempfood[3]))
            food.generate(int(tempfood[0]), int(tempfood[1]), int(tempfood[2]))
            food.generate(int(tempfood[0]), int(tempfood[1]), int(tempfood[2]))

    return snakes


def deleteblocks():
    global otherplayerblocks
    for i in range(len(otherplayerblocks)):
        SnakeGameMap.canvas.delete(otherplayerblocks[i])


def updateothers():
    global otherplayer
    global otherplayerblocks
    for i in range(len(otherplayer)):
        for j in range(len(otherplayer[i])):
            otherplayerblocks.append(
                SnakeGameMap.canvas.create_rectangle(int(otherplayer[i][j][0]), int(otherplayer[i][j][1]),
                                                     int(otherplayer[i][j][0]) + 10, int(otherplayer[i][j][1]) + 10,
                                                     fill='violetred1'))


def tick(player, found):
    deleteblocks()
    global time1
    global food
    global otherplayer
    global otherplayerblocks
    global wefoundfood
    global _x, _y, _r, _j
    time2 = time.strftime('%H:%M:%S')

    snakes = sendCoord()

    scores = calculate_score_table(snakes, username)
    player_score = player.calculate_score()
    SnakeGameMap.update_score(player_score, username, scores)
    fpga_communicator.write_hextext(str(player_score))

    if game_over:
        SnakeGameMap.show_game_over(username, player_score)
        fpga_communicator.write_ledflash("10000100001")
        fpga_communicator.write_hextext("GAME_OVER_SCORE_" + str(player_score))
        return

    array = []
    for i in range(len(snakes)):
        temparray = snakes[i]['blocks'].split(";")
        for j in range(len(temparray)):
            if len(temparray[j]) > 0:
                array.append([temparray[j].split(",")[0], temparray[j].split(",")[1]])
    otherplayer = [array]

    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    if fpga_communicator.initialized:
        acc_read = fpga_communicator.read_acc_proc()
        if 75 < acc_read['x'] < 250 and not 75 <= acc_read['y'] <= 4021:
            player.changedir('Left')
        elif 3750 < acc_read['x'] < 4021 and not 75 <= acc_read['y'] <= 4021:
            player.changedir('Right')
        elif 3750 < acc_read['y'] < 4021 and not 75 <= acc_read['x'] <= 4021:
            player.changedir('Up')
        elif 75 < acc_read['y'] < 250 and not 75 <= acc_read['x'] <= 4021:
            player.changedir('Down')
    player.movesnake()

    updateothers()

    for j in range(len(food.power_ups)):
        if (player.x == food.power_upsX[j]) and (player.y == food.power_upsY[j]):
            player.adjustspeed(1)
            food.powerupType(player, food.power_ups[j][1])
            if not game_over:
                clock.after(100, lambda: tick(player, FALSE))
            fpga_communicator.write_ledflash("1100110011")
            food.delete(j)
            _x = random.randrange(30, 500, 10)
            _y = random.randrange(20, 500, 10)
            _r = 4
            _j = j
            food.generate(_x, _y, _r)
            food.generate(_x, _y, _r)
            found = TRUE
            wefoundfood = 1
            break

    if found == FALSE and not game_over:
        clock.after(int(30 / player.getspeed()), lambda: tick(player, FALSE))


def start_game(_server_ip, _server_port, _client_port, _username):
    global server_ip, server_port, client_port, username, player, food, clock
    server_ip = _server_ip
    server_port = _server_port
    client_port = _client_port
    username = _username

    for child in root.winfo_children():
        child.destroy()

    SnakeGameMap.root = root
    SnakeGameMap.init_game()
    clock = Label(SnakeGameMap.root)
    player = SnakeGameMap.player
    food = SnakeGameMap.food

    SnakeGameMap.root.bind("<Key>", SnakeGameMap.kpress)
    tick(player, FALSE)


game_intro = GameIntro(root, start_game)
root.mainloop()
