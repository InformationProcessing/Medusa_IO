import tkinter as tk
from tkinter import *
import time
import random
import socket
import atexit
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
import components.SnakeGameMap as SnakeGameMap
from components.game_intro import GameIntro
from components.fpga_communicator import FPGACommunicator
import multiprocessing

root = tk.Tk()
fpga_communicator = FPGACommunicator()

client_port = None
server_ip = None
server_port = None
username = None
player = None
food = None
localFood = None
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
coin_sound = AudioSegment.from_wav('SnakeVisualiser/assets/coinhit.wav')
game_over_sound = AudioSegment.from_wav('SnakeVisualiser/assets/gameover.wav')


def exit_handler():
    msg = str(username) + "|0,0;|0,0,0,0,0"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('', client_port))
    client_socket.sendto(msg.encode(), (server_ip, server_port))



def mergearray(array1, array2):
    newarray = []
    for i in range(len(array1)):
        newarray.append([array1[i] + 100, array2[i] + 100])
    return newarray


def calculate_score_table(other_players, client_name):
    score_table = []

    for other_player in other_players:
        score = len(other_player["blocks"].split(";")) - 10
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
            food.deleteShared()
            food.generateShared(int(tempfood[0]), int(tempfood[1]))
            food.generateShared(int(tempfood[0]), int(tempfood[1]))

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
                                                     fill='#C7FFFD'))

def coin_sound_wrapper():
    play(coin_sound)

def game_over_sound_wrapper():
    play(game_over_sound)

def game_over_notification():
    try:
        proc = multiprocessing.Process(target=game_over_sound_wrapper)
        proc.start()
    except Exception as ex:
        print("Error with coin sound: " + str(ex))

def food_collected_notification():
    try:
        proc = multiprocessing.Process(target=coin_sound_wrapper)
        proc.start()
    except Exception as ex:
        print("Error with coin sound: " + str(ex))

    try:
        t = Thread(target=fpga_communicator.write_ledflash, args=("101",), daemon=True)
        t.start()
    except Exception as ex:
        print("Error with led flash: " + str(ex))

def tick(player, found):
    try:
        deleteblocks()
        global time1
        global food
        global localFood
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
            game_over_notification()
            player_position = SnakeGameMap.show_game_over(username, player_score)
            fpga_communicator.write_ledflash("10000100001")
            fpga_communicator.write_hextext("GAME_OVER_SCORE_" + str(player_score) + "_PLACE_" + str(player_position))
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

        if (abs(player.x - food.shared_power_upX) < food.radius and abs(player.y - food.shared_power_upY) < food.radius):
            player.adjustspeed(1)
            food.powerupType(player, "Ultra-Power")
            food.deleteShared()
            food_collected_notification()
            _x = random.randrange(30, 500, 10)
            _y = random.randrange(20, 500, 10)
            food.generateShared(_x, _y)
            wefoundfood = 1

        for i in range(0, len(localFood.power_ups)):
            if (player.x == localFood.power_upsX[i]) and (player.y == localFood.power_upsY[i]):
                player.adjustspeed(1)
                print(localFood.power_ups[i])
                localFood.powerupType(player, localFood.power_ups[i][1])
                clock.after(200, lambda: tick(player, FALSE))
                localFood.delete(i)
                food_collected_notification()
                localFood.generate()
                found = TRUE
                break

        if found == FALSE and not game_over: clock.after(int(100 / player.getspeed()), lambda: tick(player, FALSE))
    except Exception as error:
        print("Error in tick: " + str(error))


def start_game(_server_ip, _server_port, _client_port, _username):
    global server_ip, server_port, client_port, username, player, food, clock, localFood
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
    food = SnakeGameMap.sharedFood
    localFood = SnakeGameMap.localFood

    SnakeGameMap.root.bind("<Key>", SnakeGameMap.kpress)
    tick(player, FALSE)

if __name__ == "__main__":
    atexit.register(exit_handler)
    game_intro = GameIntro(root, start_game)
    root.attributes("-fullscreen", True)
    root.mainloop()