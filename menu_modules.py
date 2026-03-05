import pybuzzers
import time
import os
import sys
import controller_management, leaderboard
import questionManagement
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
    try:
        buzzer.stop_listening()
    except Exception:
        pass
    os.system('cls')
    print('Project Cortex\n\n\n\n')
    print(' 1) Start Game  2) Download Questions  3) Leaderboard  4) Exit')
    menuInput = input('>> ')
    if menuInput == ('1'):
        os.system('cls')
        print('Select Game Mode\n\n\n\n')
        print(' 1) Hosted Quiz  2) Multiquestion')
        gameSelect = input('>> ')
        if gameSelect == ('1'):
            os.system('cls')    
            print('Game Start')
            buzzer.on_buzz(controller_management.buzzIn)
            buzzer.start_listening()
            while not controller_management.end_game_requested:
                time.sleep(0.1)
            controller_management.end_game_requested = False
            mainMenu()
            return
        elif gameSelect == ('2'):
            ## COME BACK TO THIS ONCE QUESTIONS HAVE BEEN IMPLIMENTED
            os.system('cls')
            print('Multiquestion Mode')
            questionManagement.reset_question_pool()
            controller_management.show_random_question()
            buzzer.on_button_down(controller_management.multiBuzz)
            time.sleep(1)
            mainMenu()
    elif menuInput == ('2'):
        os.system('cls')
        print('Contacting the TeamOrbi servers...')
        time.sleep(1)
        mainMenu()
    elif menuInput == ('3'):
        leaderboard.leaderboard_menu()
        mainMenu()
    elif menuInput == ('4'):
        sys.exit(0)
