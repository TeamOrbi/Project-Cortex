import os


def playerAdjust(Buzzer):
    if Buzzer == 0:
        update_leaderboard('Player 1', 10)
    elif Buzzer == 1:
        update_leaderboard('Player 2', 10)
    elif Buzzer == 2:
        update_leaderboard('Player 3', 10)
    elif Buzzer == 3:
        update_leaderboard('Player 4', 10)


def update_leaderboard(player_name, score):
    with open('leaderboard.txt', 'a') as file:
        file.write(f"{player_name}: {score}\n")

def read_leaderboard():
    with open('leaderboard.txt', 'a') as file:
        print(file)


def reset_leaderboard():
    if os.path.exists('leaderboard.txt'):
        os.remove('leaderboard.txt')
    else:
        print('There is no Leaderboard to remove.')

def leaderboard_menu():
    os.system('cls')
    print('1) View Leaderboard 2) Clear Leaderboard 3) Return to Menu')
    leadermenuInput = input('>> ')
    if leaderboard_menu == ('1'):
        read_leaderboard()
    elif leaderboard_menu == ('2'):
        reset_leaderboard()
    elif leaderboard_menu == ('3'):
        return()