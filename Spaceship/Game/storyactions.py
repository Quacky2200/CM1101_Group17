from story import *
from gameparser import *
from conversations import *
import player
from time import sleep
"""
Now we've sorted the basic storyline, we can add the dynamic story. We can now change things like rooms, inventory, items, characters etc...

For example
    def use_id():
        print('Beep Boop! (You've just signed in)')

    def drop_biscuits():
        item_biscuits['description'] = 'Crumbled biscuits... Not so yummy anymore.'

"""
squirrel_chase = False
def use_torch(item_id1, item_id2):
    if player.current_room['name'] == room_forest['name']:
        room_forest['description'] = "The battery is quite low and the light starts to flicker. Luckily, \nyou catch a glimpse of a rocky surface and smoke rising in the distance towards the east...The \ntorch turns off before you see anything else."
        room_forest['exits']['east'] = room_caves['name']
        del room_blindlydark['exits']['south']
drinking_amount = 0
def drink():
    global drinking_amount
    if drinking_amount != 3: 
        print('Drinking makes you feel weak and unsteady. Yuck!')
    elif drinking_amount == 3:
        print('You throw up!')
        drinking_amount = 0
    drinking_amount += 1
def use_rum(item_id1, item_id2):
    drink()
    player.inventory.remove(item_rum)
def use_pepper(item_id1, item_id2):
    print('It tastes great, shame there isn\'t anymore in the bottle. I feel so hyped! :D')
    player.inventory.remove(item_pepper)
def use_beer(item_id1, item_id2):
    drink()
    player.inventory.remove(item_beer)
def use_rivet(item_id1, item_id2):
    item1 = None
    item2 = None
    for item in player.inventory:
        if item['id'] == item_id1:
            item1 = item
        elif item['id'] == item_id2:
            item2 = item
    if item1 == item_rivetgun and item2 == item_scrapmetal and item_scrapmetal['description'] == 'This should work on my spaceship now' and player.current_room['name'] == room_spaceship['name']:
        player.inventory.remove(item2)
        player.hole_replaced = True
    elif item1 == item_rivetgun and item2 == item_fueltank and player.current_room['name'] == room_spaceship['name']:
        player.inventory.remove(item2)
        player.fuel_tank_installed = True
def use_fuel_canister(item_id1, item_id2):
    item1 = None
    item2 = None
    for item in player.inventory:
        if item['id'] == item_id1:
            item1 = item
        elif item['id'] == item_id2:
            item2 = item
    if item1 == item_fuelcanister and item2 == None and player.current_room['name'] == room_spaceship['name']:
        player.inventory.remove(item1)
        player.fuel_installed = True
def out_caves():
    global squirrel_chase
    if not squirrel_chase:
        cave_issue = 'On your way back to the forest, you encounter a wild looking squirrel. \nThe squirrel starts drooling and it\'s eyes start looking wild and \ndazed. It starts coming towards you...'
        throw = ['You have hardly any energy from the spaceship crash, the squirrel is unharmed from your weak throw and looks even more hungry...','You have nothing left to throw now that you just threw your torch']
        kick = ['The squirrel starts nibbling on your leg, you can hardly let go because of how tired you are.', 'You kick again but to no use ']
        run =['You slowly start running but it\'s still chasing you. The muscle ache from the crash and moving people seem to be hindering your success', 'you think you have just escaped it so you start to slow down but it catches up to you']
        scream =['Nothing much comes out of your dry mouth except a tiny squeek. The rabid squirrel is getting closer', 'you scream louder but nothing seems to be hindering this little rabid squirrel']
        i = 0
        while i != 2:
            print(cave_issue)
            print('\nYou can:\nRUN to run away\nKICK to kick it\nSCREAM to scream at (something?)')
            output = normalise_input(input('What do you want to do?\n'))
            if output[0] == 'throw':
                if not item_torch['name'] in [item['name'] for item in player.inventory]:
                    cave_issue = 'You realise you dropped it earlier, you just wasted a precious moment to survive from this rabid squirrel'
                else:
                    cave_issue = throw[0]
                    throw.remove(throw[0])
                    for item in player.inventory:
                        if item['id'] == item_torch['id']:
                            player.inventory.remove(item)
                            break
            elif output[0] == 'run':
                cave_issue = run[0]
                run.remove(run[0])
            elif output[0] == 'kick':
                cave_issue = kick[0]
                kick.remove(kick[0])
            elif output[0] == 'scream':
                cave_issue = scream[0]
                scream.remove(scream[0])
            i += 1
        if len(run) <= 1:
            print(cave_issue)
            print("\n\n*BOOM*\n\nThe sound of a shotgun reverberates. The squirrel explodes everywhere and blood splats all around it. Luckily, \nthe squirrel was small enough to only cover your knees in blood. You hear footsteps from the rustling leaves. \nYou turn around and...\n")
            room_cabin['exits']['south'] = room_forest['name']
            player.current_room = room_cabin
            talk(character_hunter['conversation'])
        else:
            print('The rabid squirrel was so excessively hungry that it jumped on top of you and \nstarted eating at your neck, it ripped out an artery. You\'re dead.')
            quit()
        squirrel_chase = True
        room_caves['description'] = 'The tribesmen are looking after your crew fantastically. They\'ve been using \nherb remedies to remove most of the pain and have removed some of \nthe burns, scars and blood. They\'re looking happier but not their best. \nThey still aren\'t able to do work in their situation. The campfire wamth has \ndampened down leaving the sunlight to be a weak substitute. An old \nrabbit is on the fire from last night. Not much has been eaten, \nthey\'re probably using it over a week.'
def out_forest():
    if player.hole_replaced and player.fuel_tank_installed and player.fuel_installed:
        room_caves['description'] = 'Your crew are gone and so are the tribesmen, you get really worried \nlooking around until you\'ve found blood along a footpath that has a sign saying "Mountains"'
def take_scrap():
    conversation_manager['output'][1]['output'].append(['I\'d like this scrap metal cut for me, please?', {
        'who': character_manager['name'],
        'output': ['Okie Dokie! That\'s why we\'re here!', fix_scrap]
    }])
def in_forest():
    if item_torch in player.inventory:
        item_torch['enabled'] += [drop, use]
def recieved_mountains():
    if not item_boots in player.current_room['items']: print('They accept your item and let one of your crew go')
    if item_map in room_spaceship['items'] and item_rivetgun in player.current_room['items'] and item_torch in player.current_room['items'] and item_money in player.current_room['items'] :
        print("""You now have all of your crew. The tribemens are happy that you gave them items 
for taking care of your crew. It's fair to say that Mayor Quimby won't be getting his fuel canister back, 
nor will the manager get his rivet gun. You all went down the mountain quickly because you were excited of 
showing them your new creation. When you and your crew came down and got in the spaceship, the metal you 
riveted on, comes off. The fuel tank also falls to the floor. When you and your crew realise that all you 
needed was the Mayors telephone, the only thing you can express is embarassment for letting your crew go 
through all that pain. 

The End. 

YOU WON!!!!!!""")
        quit()
def in_blindlydark():
    print(player.current_room['description'])
    print('')
    sleep(2.2)
    player.current_room = room_forest
#Now everything else is completed, we can add the most important parts because the rooms/items/characters have been referenced
item_actions = {
    item_pepper['id']: {use:use_pepper},
    item_beer['id']: {use:use_beer},
    item_rum['id']: {use:use_rum},
    item_torch['id']: {use: use_torch},
    item_rivetgun['id']: {use: use_rivet}, 
    item_fuelcanister['id']: {use: use_fuel_canister},
    item_scrapmetal['id']: {take: take_scrap}
    }

room_actions = {
    room_blindlydark['name']:{'in':in_blindlydark, 'out':None},
    room_forest['name']:{'in':in_forest, 'out': out_forest},
    room_caves['name']:{'out': out_caves},
    room_mountain['name']:{'recieve':recieved_mountains}
    }

character_actions = {
    character_tribe['name']: {'talk': talk},
    character_barman['name']: {'talk': talk},
    character_mayor['name']: {'talk': talk},
    character_sailor['name']: {'give': None, 'talk': talk},
    character_hunter['name']: {'give': None, 'talk': talk},
    character_manager['name']: {'talk': talk}
    }

#Unrelated here...
from datetime import *
def add_seconds(seconds):
    #Simplified:
    # if (datetime.now() + seconds) >= 60:
    #     return datetime.now().second - seconds
    # else:
    #     return datetime.now().second + seconds
    return ((datetime.now().second - seconds) if (datetime.now().second + seconds) >= 60 else (datetime.now().second + seconds))