from orbiLib import updateCheck, type_message
import menu_modules, controller_management, leaderboard
import pybuzzers
import time


version = '0.1.0'

type_message('A Team Orbi Production', 0.1)
type_message('Checking for updates...')
updateCheck(version)
time.sleep(0.2)
type_message('Checking Options...')
##Add options that need checking here
print('The options have been Checked!')
buzzer = pybuzzers.get_all_buzzers()[0]
menu_modules.loadingLights(buzzer)
print('Buzzers Connected')
type_message('Intializing Buzzers...')
print('Buzzers Ready')
time.sleep(0.2)
type_message('Resetting The Leaderboard...')
leaderboard.reset_leaderboard()
print('Leaderboard Reset.')
time.sleep(0.2)
menu_modules.mainMenu()
