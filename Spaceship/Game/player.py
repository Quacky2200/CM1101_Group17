import os
from gameparser import *
from time import sleep
inventory = None
max_weight = 80.05
current_room = None
hole_replaced = False
fuel_tank_installed = False
fuel_installed = False
username = ''
def clear():
	if os.name != 'nt': 
		os.system('clear')
	else:
		os.system('cls')
def print_wait(message, time = 1):
	print(message)
	sleep(time)
while username == '':
	clear()
	username = ' '.join(normalise_input(input('Your name, please?\n'))).title()
clear()
print_wait('Well hello there... ' + username, 2)
clear()