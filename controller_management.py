import pybuzzers
import time
import leaderboard
import options

ControllerInput = True
_last_buzz_time = {}
_buzz_cooldown_seconds = 0.75
_arm_time = 0.0
_arm_delay_seconds = 1.0
_last_buzzer_id = None


def _set_buzzer_light(buzzer_set: pybuzzers.BuzzerSet, buzzer: int, state: bool):
    # Best-effort: pybuzzers exposes set_light on the buzzer device.
    try:
        buzzer_set.set_light(buzzer, state)
    except Exception:
        pass

def buzzIn(buzzer_set: pybuzzers.BuzzerSet, buzzer: int):
    global ControllerInput, _arm_time, _last_buzzer_id
    now = time.time()
    if now - _arm_time < _arm_delay_seconds:
        return
    last = _last_buzz_time.get(buzzer, 0.0)
    if now - last < _buzz_cooldown_seconds:
        return
    _last_buzz_time[buzzer] = now
    if ControllerInput == True:
        ControllerInput = False
        _last_buzzer_id = buzzer
        _set_buzzer_light(buzzer_set, buzzer, True)
        print(f"Player {buzzer} buzzed!")
        isCorrect = input('Did they get it correct? (y/n) ')
        if isCorrect and isCorrect.lower() == 'y':
            leaderboard.playerAdjust(buzzer)
            if options.show_leaderboard:
                leaderboard.read_leaderboard()
        # Lock input until the host advances to the next question.
        input('Press Enter to enable buzzing for the next question...')
        if _last_buzzer_id is not None:
            _set_buzzer_light(buzzer_set, _last_buzzer_id, False)
            _last_buzzer_id = None
        _arm_time = time.time()
        _last_buzz_time.clear()
        ControllerInput = True

