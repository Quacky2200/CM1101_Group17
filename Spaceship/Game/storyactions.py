from story import *
import player
"""
Now we've sorted the basic storyline, we can add the dynamic story. We can now change things like rooms, inventory, items, characters etc...

For example
    def use_id():
        print('Beep Boop! (You've just signed in)')

    def drop_biscuits():
        item_biscuits['description'] = 'Crumbled biscuits... Not so yummy anymore.'

"""
def use_torch(item_id1, item_id2):
    if player.current_room['name'] == room_forest['name']:
        room_forest['description'] = "The battery is quite low and the light starts to flicker. Luckily, \nyou catch a glimpse of a rocky surface and smoke rising in the distance towards the east...The \ntorch turns off before you see anything else."
        room_forest['exits']['east'] = room_caves['name']

def in_forest():
    if item_torch in player.inventory:
        item_torch['enabled'] += [drop, use]
def out_forest():
    #print('This was printed using the "out" event')
    #Move characters/change scenery etc when we've done everything
    pass

drinking_amount = 0
def use_rum(item_id1, item_id2):
    #Makes me feel drowsy
    if drinking_amount != 3: 
        print('Drinking makes you feel weak and unsteady. Yuck!')
    elif drinking_amount == 3:
        print('You throw up!')
        drinking_amount = 0
    drinking_amount += 1

def use_boots(item_id1, item_id2):
    #I can now climb a mountain
    pass
#Now everything else is completed, we can add the most important parts because the rooms/items/characters have been referenced
item_actions = {
    item_torch['id']: {take: None, drop: None, use: use_torch},
    }

room_actions = {
    room_forest['name']:{'in':in_forest, 'out': None},
    room_caves['name']:{'in': None,'out': None}
    }

character_actions = {
    character_sailor['name']: {'give': None, 'talk': None},
    character_hunter['name']: {'give': None, 'talk': None}
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