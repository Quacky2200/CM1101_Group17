from items import *

room_reception = {
    "name": "Reception",

    "description": "Matt Strangis is looking desperately for his items, can you find them?",

    "exits": {"south": "Robs", "east": "Tutor", "west": "Lecture"},

    "items": [item_biscuits, item_handbook],

    "given_items": []
}
room_labs = {
    "name": "Labs",

    "description": "Room full of Windows computers and confused students (trying to learn Python)",

    "exits": {'north': 'Robs'},

    "items": [item_laptop]
}
room_lecture = {
    "name": "Lecture Theatre",

    "description": "Boring...",

    "exits": {'east': 'Reception', 'down': 'Refectory'},

    "items": [item_money]
}
room_refectory = {
    "name": "Refectory",

    "description": "Food glorious food...(mmmm)...",

    "exits": {'south': 'Parking', 'up':'Lecture'},

    "items": [item_lunchbox, item_waterbottle]
}

room_robs = {
    "name": "Robs' room",

    "description": "They are all way too busy playing a text-based adventure game",

    "exits":  {"north": "Reception", 'south': 'Labs'},

    "items": [item_coffee]
}

room_tutor = {
    "name": "your personal tutor's office",

    "description": "He's not in his office, that curry on the table stinks and he has a cold, so I suspect he's in the toilet.",

    "exits": {"west": "Reception"},

    "items": [item_pen]
}

room_parking = {
    "name": "the parking lot",

    "description": "Most of the cars are still the lecturers' first cars",

    "exits": {"east": "Office", "north": "Reception"},

    "items": [item_blackbriefcase, item_lostkeys]
}

room_office = {
    "name": "the general office",

    "description": "Nothing but stapling sheets of paper and the sound of printing. Oh and the scruffy registers.",

    "exits": {"west": "Parking"},

    "items": [item_chair]
}



rooms = {
    "Reception": room_reception,
    "Robs": room_robs,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office,
    "Labs": room_labs,
    "Refectory": room_refectory,
    "Lecture": room_lecture,

}
