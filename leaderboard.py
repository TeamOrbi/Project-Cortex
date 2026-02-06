
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