from gameparser import *
import os
from time import sleep
inventory = None
max_weight = 80.05
current_room = None
hole_replaced = False
fuel_tank_installed = False
squirrel_chase = False
fuel_installed = False
username = ''
def clear():
    if os.name != 'nt': 
        os.system('clear')
    else:
        os.system('cls')
while username == '':
	clear()
	username = ' '.join(normalise_input(input('Your name, please?\n'))).title()
clear()
print('Well hello there... ' + username)
sleep(1)
clear()