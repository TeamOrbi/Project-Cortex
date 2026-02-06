import pybuzzers
import leaderboard

def buzzIn(buzzer_set: pybuzzers.BuzzerSet, buzzer: int):
    print(f"Player {buzzer} buzzed!")
    isCorrect = input('Did they get it correct? (y/n)')
    if isCorrect == 'y' or 'Y':
        leaderboard.playerAdjust({buzzer})

