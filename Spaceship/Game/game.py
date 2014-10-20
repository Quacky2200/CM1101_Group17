#!/usr/bin/python3
from storyactions import *
from gameparser import *
import player
from time import sleep
converses = {'north':'south', 'east':'west', 'up':'down', 'left':'right', 'inside':'outside', 'upstairs':'downstairs'}
def print_wait(str, time = 1):
    print(str)
    sleep(time)
def weight_of_items(items):
    """This function takes a list of items and returns the total weight 
    from the whole list. Some of the items will be in grams and kilograms 
    and need to be translated into KG for the final total. The expected
    return result is a string. For Example:

    >>> weight_of_items([item_pen, item_handbook])
    0.752

    >>> weight_of_items([])
    0

    """
    result = []
    for item in items:
        if 'kg' in item['weight'].lower():
            result.append(float(item['weight'].lower().replace('kg', '')))
        else:
            result.append(float(item['weight'].lower().replace('g','')) / 1000)
    return sum(result)
def return_converse(text):
    """ This function allows us to return the reverse of a direction 
    such as North is the converse of South. It has to use the converses dictionary 
    so you can add your own. For Example:
    >>> return_converse('north')
    'south'
    >>> return_converse('up')
    'down'
    >>> return_converse('')

    """
    if text in converses.keys():
        return list(converses.values())[list(converses.keys()).index(text)]
    elif text in converses.values():
        return list(converses.keys())[list(converses.values()).index(text)]
def fix_exits():
    for room in rooms:
        for direction, leads_to in rooms[room]['exits'].items():
            if not return_converse(direction) in rooms[leads_to]['exits']:
                rooms[leads_to]['exits'][return_converse(direction)] = room
def item_in_inventory(item_id, enabled = ''):
    if enabled != '':
        return item_id in [item['id'] for item in player.inventory if enabled in item['enabled']]
    else:
        return item_id in [item['id'] for item in player.inventory]
#Normal
def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'an id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    result = ''
    for item in items:
        result += item['name'] + (', ' if not item == items[len(items) - 1] else '')
    return result
def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a chair here.
    <BLANKLINE>

    >>> print_room_items(rooms["Robs"])
    There is hot coffee here.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(room['items']) != 0:
        print("There is " + list_of_items(room['items']) + " here.")
        print("")
def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have an id card.
    <BLANKLINE>

    """
    if len(items) > 0:
        print("You have " + list_of_items(items) + ".")
        print('')
def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    Nothing but stapling sheets of paper and the sound of printing. Oh and the scruffy registers.
    <BLANKLINE>
    There is a chair here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    Matt Strangis is looking desperately for his items, can you find them?
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    They are all way too busy playing a text-based adventure game
    <BLANKLINE>
    There is hot coffee here.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")
    print_room_items(room)
def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]
def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")
def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in [items for items in room_items if 'take' in items['enabled']]:
        print('TAKE ' + item['id'].upper() + ' to take ' + item['name'])
    for item in [items for items in inv_items if 'drop' in items['enabled']]:
        print('DROP ' + item['id'].upper() + ' to drop your ' + item['id'])
    for item in [items for items in inv_items if 'use' in items['enabled']]:
        print('USE ' + item['id'].upper() + ' to use your ' + item['id'])
    print("What do you want to do?")
def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits
def execute_item_action(item_id, action, item_id2 = ''):
    if item_id in item_actions:
        itemaction = item_actions[item_id]
        if action in itemaction.keys():
            if itemaction[action] != None and callable(itemaction[action]):
                if action == use:
                    itemaction[action](item_id, item_id2)
                else:
                    itemaction[action]()
def execute_character_action(charactername, action, item_id = ''):
    if charactername in character_actions.keys():
        characteraction = character_actions[charactername]
        if action in characteraction:
            if characteraction[action] != None and callable(characteraction[action]):
                if item_id != '':
                    characteraction[action](item_id)
                else:
                    characteraction[action](charactername)
def execute_room_action(action):
    if player.current_room['name'] in room_actions.keys():
        roomaction = room_actions[player.current_room['name']]
        if action in roomaction:
            if roomaction[action] != None and callable(roomaction[action]):
                roomaction[action]()
def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if is_valid_exit(player.current_room['exits'], direction):
        #Run 'out' action if there is one 
        execute_room_action('out')
        #Swap rooms
        player.current_room = move(player.current_room['exits'], direction)
        #Run the 'in' action if there is one
        execute_room_action('in')
    else:
        print("You cannot go there.")
def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    for item in [items for items in player.current_room['items'] if take in items['enabled']]:
        tempinventory = player.inventory[:]
        tempinventory.append(item)
        if item['id'] == item_id and weight_of_items(tempinventory) < max_weight and len(player.inventory) < 4:
            player.inventory.append(item)
            player.current_room['items'].remove(item)
            execute_item_action(item['id'], 'take')
            return
        elif item['id'] == item_id and weight_of_items(tempinventory) > max_weight or len(player.inventory) == 4:
            print('You only have 2 hands (and a full bag)')
            return
    print('You cannot take that.')
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    for item in [items for items in player.inventory if drop in items['enabled']]:
        if item['id'] == item_id:
            player.current_room['items'].append(item)
            player.inventory.remove(item)
            execute_item_action(item['id'], 'drop')
            return
    print('You cannot drop that.')
def execute_give(item_id, person):
    if item_in_inventory(item_id):
        for character in player.current_room['characters']:
            if character['name'].replace(' ', '').lower() == person:
                execute_character_action(character['name'],'give', item_id)
                return
    print('You cannot give that')
def execute_use(item_id1, item_id2 = ''):
    if item_id2 != '':
        if item_in_inventory(item_id1, use) and item_in_inventory(item_id2, use):
            return_item_action(item_id1, use, item_id2)
            return
    else:
        if item_in_inventory(item_id1, use):
            execute_item_action(item_id1, use)
            return
    print('You cannot use that')
def execute_talk(person):
    for character in player.current_room['characters']:
        if character['name'].replace(' ','').lower() == person:
            execute_character_action(character['name'],'talk')
            return
    print('Who\'s that?')
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if len(command) == 0:
        print_wait('Nothing was entered...')
        return
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print_wait("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print_wait("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print_wait("Drop what?")
    elif command[0] == 'give':
        if len(command) > 1:
            execute_give(command[1])
        else:
            print_wait('Give what?')
    elif command[0] == 'use':
        if len(command) > 1:
            if len(command) == 3:
                execute_use(command[1], command[2])
            else:
                execute_use(command[1])
        else:
            print_wait('Use what?')
    elif command[0] == 'talk':
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print_wait('Talk to whom?')
    elif command[0] == "quit":
        #Check if the player wants to continue, otherwise they risk losing their game progress accidentally.
        check = input("Quitting will not save game progress, continue? (Y/N): ")
        checkvalue = (check.split()[0].lower() if len(check) != 0 else execute_command(command))
        #Get the first word, we don't care about the others, and also make it lowercase (e.g. yEs PlEaSe = yes) 
        #if they entered something, otherwise, repeat the question
        if checkvalue == 'y' or checkvalue == 'yes': #We can now check the two values easily
            quit() #Only quit if they said yes
    else:
        print_wait("This makes no sense.")
def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input
def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Robs"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]
# This is the entry point of our program
def main():

    # Main game loop
    while True:
            # Display game status (room description, inventory etc.)
            print_room(player.current_room)
            print_inventory_items(player.inventory)

            # Show the menu with possible actions and ask the player
            command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)

            # Execute the player's command
            execute_command(command)

            fix_exits()
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

