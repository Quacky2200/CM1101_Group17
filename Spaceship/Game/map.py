from items import *

room_jungle = {
    "name": "jungle",

    "description": "A vast landscape full of dense trees and shrubs. Insects can be heard in the bushes.",

    "exits": {"south": "Beach", "east": "cave", "west": "Town", "north": "cabin", "in": "spaceship"},

    "items": [item_biscuits, item_handbook],

    "given_items": []
}
room_spaceship = {
    "name": "spaceship",

    "description": "The spaceship that I crash landed in, it's in a bad state, i'm going to have to try and fix it.",

    "exits": {'outside': 'jungle'},

    "items": [item_laptop]
}
room_cabin = {
    "name": "cabin",

    "description": "A hunter's cabin, fully decorated with trophies from around the land.",

    "exits": {'east': "mountain", 'south': 'jungle'},

    "items": [item_money]
}
room_cave = {
    "name": "cave",

    """description": "The cave is narrow to start with but expands out into a large cavern area where a tribe of people
    are sat around a campfire cooking and chatting.""",

    "exits": {'west': 'jungle', 'north':'mountain'},

    "items": [item_lunchbox, item_waterbottle]
}

room_beach = {
    "name": "Beach",

    "description": """Golden sand and clear blue waters, looks like a great place for a summer holiday. There's a 
    shipwrecked boat on the land close by, maybe I should investigate.""",

    "exits":  {"north": "jungle", 'inside': 'shipwreck'},

    "items": [item_coffee]
}

room_town = {
    "name": "Town",

    "description": """The Town, a modern looking place with office buildings occupying a lot of the seeable landscape, 
    a few other shops appear to be scattered throughout the place. Luckily the town has a bar...""",

    "exits": {"inside": "pub", "north": "hardware", "south": "Mayors"},

    "items": [item_pen]
}

room_mayor = {
    "name": "Mayors house",

    "description": """T""he mayor of the town's house, looks like he is paid very well. His house is enormous with lavish
    paintings of himself placed in pretty much every room, luxurious furniture everywhere... this man clearly has a lot of power""",

    "exits": {"outside": "Town"},

    "items": [item_blackbriefcase, item_lostkeys]
}

room_bar = {
    "name": "bar",

    "description": """An old western themed tavern with bar stools littered around the circle tables. A pool table in one corner
    next to a jukebox playing what sounds like the theme from 'The Good, the Bad and the Ugly'. There's a crowd of people watching
    a boxing match on the T.V., while one patron is passed out in a pool of his own sick... classy place, maybe the bar tender
    can tell me more about this place... """,

    "exits": {"outside": "Town", "upstairs": "room 101"},

    "items": [item_chair]
}
room_room101 = {
    "name": "room 101",

    "description": """A hirable room that can be rented from the bar keep. There's not much in the room, a bed, a small wardrobe
    a little desk and a toilet, the bare essentials. There are some dubious stains on the curtains and what looks like blood on the
    end of the desk... probably best not to ask questions.""",

    "exits": {"downstairs": "bar"},

    "items": [item_]
}

room_hardware = {
    "name": "hardware store",

    "description": """A small store that has a large scrapyard out the back with lots of spare parts and tools lying about
    maybe I should ask the owner if he can help me fix my ship. """,

    "exits": {"south": "Town"},

    "items": [item_]
}

room_shipwreck = {
    "name": "shipwreck",

    "description": """An old looking pirate ship that must have come aground during a storm. The whole ship is rotting away in the sand
    but a name is still enscribed on the side of the boat, THE GILDED LADY, hmm sounds familiar... """,

    "exits": {"outside": "Beach"},

    "items": [item_chair]
}
room_mountain = {
    "name": "The mountains",

    "description": """The mountain range contains several high peaks covered with snow, a shaky wooden bridge connects
    the only way through the pass, several boards are missing... The tribe must have gone this way with my friends.""",

    "exits": {"west": "cabin", "climbing": "cave"},

    "items": [item_chair]
}



rooms = {
    "spaceship": room_spaceship,
    "cabin": room_cabin,
    "cave": room_cave,
    "Town": room_town,
    "Beach": room_beach,
    "jungle": room_jungle,
    "shipwreck": room_shipwreck,
    "mountain": room_mountain,
    "hardware": room_hardware,
    "Mayors": room_mayor,
    "bar": room_bar

}
