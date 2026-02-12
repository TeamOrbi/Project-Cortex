import os
import time

def playerAdjust(Buzzer):
    if Buzzer == 0:
        update_leaderboard('Player 1', 10)
    elif Buzzer == 1:
        update_leaderboard('Player 2', 10)
    elif Buzzer == 2:
        update_leaderboard('Player 3', 10)
    elif Buzzer == 3:
        update_leaderboard('Player 4', 10)
    else:
        print('PLAYER AJUST ERROR')
        print(Buzzer)

def update_leaderboard(player_name, score):
    entries = {}
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if ':' in line:
                    name, sc = line.split(':', 1)
                    try:
                        entries[name] = int(sc)
                    except ValueError:
                        entries[name] = 0
    # Add to existing score instead of replacing
    previous = entries.get(player_name, 0)
    try:
        increment = int(score)
    except ValueError:
        increment = 0
    entries[player_name] = previous + increment
    with open('leaderboard.txt', 'w', encoding='utf-8') as file:
        for name, sc in entries.items():
            file.write(f"{name}:{sc}\n")

def read_leaderboard():
    if not os.path.exists('leaderboard.txt'):
        print('No leaderboard yet.')
        return
    with open('leaderboard.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        if contents:
            print(contents)
        else:
            print('Leaderboard is empty.')


def reset_leaderboard():
    if os.path.exists('leaderboard.txt'):
        os.remove('leaderboard.txt')
    else:
        print('There is no Leaderboard to remove.')

def leaderboard_menu():
    os.system('cls')
    print('1) View Leaderboard 2) Clear Leaderboard 3) Return to Menu')
    leadermenuInput = input('>> ')
    if leadermenuInput == '1':
        read_leaderboard()
        time.sleep(1)
        return
    elif leadermenuInput == '2':
        reset_leaderboard()
        time.sleep(1)
        return
    elif leadermenuInput == '3':
        return