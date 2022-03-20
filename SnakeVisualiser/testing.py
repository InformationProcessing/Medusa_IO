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
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
import components.SnakeGameMap as SnakeGameMap
from components.game_intro import GameIntro
from components.fpga_communicator import FPGACommunicator
import multiprocessing

coin_sound = AudioSegment.from_wav('assets/coinhit.wav')

# def food_collected_notification():
#     # try:
#     #     t = Thread(target=fpga_communicator.write_ledflash, args=("101",), daemon=True)
#     #     t.start()
#     # except Exception as ex:
#     #     print("Error with led flash: " + str(ex))
#
#     p1 = multiprocessing.Process(target=play, args=(coin_sound,))
#     p1.start()
#     p1.join()
#     play(coin_sound)
#     print("playes sound")
#     try:
#         t = Thread(target=play, args=(coin_sound,), daemon=True)
#         t.start()
#     except Exception as ex:
#         print("Error playing the sound: " + str(ex))
#
# print("Here")
# food_collected_notification()
# print("Here")


from multiprocessing import Process, Queue

def rand_num(coin_sounds):
    play(coin_sounds)
    print("playes sound")

if __name__ == "__main__":
    process = Process(target=rand_num, args=(coin_sound,))
    process.start()
    print("done")
