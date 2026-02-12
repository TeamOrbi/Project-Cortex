import pybuzzers
import time
import os
import controller_management, leaderboard
buzzer = pybuzzers.get_all_buzzers()[0]

def loadingLights(buzzer):
    for count in range(1):
            for i in range(4):
                buzzer.set_light(i, True)
                time.sleep(0.5)

            for i in range(4):
                buzzer.set_light(i, False)
                time.sleep(0.5)

def mainMenu():
    os.system('cls')
    print('Project Cortex\n\n\n\n')
    print(' 1) Start Game  2) Download Questions  3) Leaderboard  4) Exit')
    menuInput = input('>> ')
    if menuInput == ('1'):
         os.system('cls')
         print('Game Start')
         buzzer.on_buzz(controller_management.buzzIn)
         buzzer.start_listening()
    elif menuInput == ('2'):
         print('Not Added Yet')
         time.sleep(1)
         mainMenu()
    elif menuInput == ('3'):
         leaderboard.leaderboard_menu()
         mainMenu()
