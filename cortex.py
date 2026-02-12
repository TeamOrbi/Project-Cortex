from orbiLib import updateCheck, type_message
import menu_modules, controller_management
import pybuzzers
import time


version = '0.0.3'

type_message('A Team Orbi Production', 0.1)
type_message('Checking for updates...')
updateCheck(version)
buzzer = pybuzzers.get_all_buzzers()[0]
menu_modules.loadingLights(buzzer)
print('Buzzers Connected')
type_message('Intializing Buzzers...')
buzzer.on_buzz(controller_management.buzzIn)
buzzer.start_listening
print('Buzzers Enabled')
time.sleep(0.2)
menu_modules.mainMenu()
