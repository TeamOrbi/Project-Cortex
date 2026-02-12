import pybuzzers
import leaderboard
import options

def buzzIn(buzzer_set: pybuzzers.BuzzerSet, buzzer: int):
    print(f"Player {buzzer} buzzed!")
    isCorrect = input('Did they get it correct? (y/n) ')
    if isCorrect and isCorrect.lower() == 'y':
        leaderboard.playerAdjust(buzzer)
        if options.show_leaderboard:
            leaderboard.read_leaderboard()
        

