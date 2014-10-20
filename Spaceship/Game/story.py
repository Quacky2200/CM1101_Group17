import player
#Item actions that can be enabled
take = 'take'
drop = 'drop'
use = 'use'
give = 'give'
#We list the items first so that we can add them to the rooms later
item_rum = {
    'id': 'rum',

    'name': 'a bottle of rum',

    'description':'a strong alcoholic beverage',

    'weight': '500G',

    'enabled': [take, drop, use, give]

    }
item_money = {
    'id': 'money',

    'name': 'some money',

    'description':'100 coins',

    'weight': '40G',

    'enabled': [take, drop, use, give]
    }
item_boots = {
    'id': 'boots',

    'name': 'a pair of hiking boots',

    'description':'Comfy and useful when going up mountains',

    'weight': '30G',

    'enabled': [take, drop, use, give]
    }
item_pump = {
    'id': 'pump',

    'name': 'a petrol pump',

    'description':'Provides a costly service',

    'weight': '500G',

    'enabled': [take, drop, use, give]
    }
item_fueltank = {
    'id': 'fueltank',

    'name': 'a fueltank',

    'description':'commonly found in cars to carry their fuel',

    'weight': '80KG',

    'enabled': [take, drop, use, give]
    }
item_fuelcanister = {
    'id': 'fuelcanister',

    'name': 'a fuel canister',

    'description':'Carries fuel, what else.',

    'weight': '20KG',

    'enabled': [take, drop, use, give]
    }
item_map = {
    'id': 'map',

    'name': 'a map',

    'description':'a map that shows most of the world',

    'weight': '20G',

    'enabled': [take, drop, use, give]
    }
item_scrapmetal = {
    'id': 'scrapmetal',

    'name': 'a piece of scrap metal',

    'description':'Won\'t fit the spaceship',

    'weight': '500G',

    'enabled': [take, drop, use, give]
    }
item_rivetgun = {
    'id': 'rivetgun',

    'name': 'a rivet gun',

    'description':'uses rivets to put to pieces of material together',

    'weight': '40G',

    'enabled': [take, drop, use, give]
    }
item_torch = {
    'id': 'torch',

    'name': 'a torch',

    'description': 'Doesn\'t do much in a text-based adventure game',

    'weight': '30G',

    'enabled': [take, drop, use, give]
    }
#Characters need to be referenced so we can add them to the rooms and so they can carry existing items (above)
character_sailor = {
    'name': 'Pete',

    'description': 'A drunk babbling sailor',

    'items': [item_money, item_map]
}
character_mayor = {
    'name': 'Quimby',

    'description': 'Proud of his town and the ambitions he wants to aspire to',

    'items': []
}
character_hunter = {
    'name': 'Rodney',

    'description': 'Proud of his wooden cabin and all the animals he has killed',

    'items': [item_boots]
}
character_tribe = {
    'name': 'Chief Powhatan',

    'description': 'Speaks nonsense, we simply can\'t understand what he says, but for some reason we trust him',

    'items': []
}
# character_engineer = {
#     'name': 'Max',

#     'description': '',

#     'items': []
# }
# character_scientist = {
#     'name': 'Arthur',

#     'description': '',

#     'items': []
# }
character_barman = {
    'name': 'Barman',

    'description': 'Loves local gossip and gives bad relationship advice.',

    'items': [item_rum]
}
#Rooms now need to be added (least important - children first)
room_mountain = {
    'name': 'the Mountains',

    'description': """The mountain spans for miles around you, high snow-covered peaks surround a small camp where 
    the Tribes' people are hiding. Large pens are visible, clearly herding mountain goats and other animals for the
    Tribes people to use in their day to day lives. """, 

    'exits': {},

    'items': [],

    'characters': []
}
room_shipwreck = {
    'name': 'the shipwreck',

    'description': """An old looking ship that must have come aground during a storm. The whole ship is rotting 
    away in the sand, making the name impossible to read. This is a sad sight, maybe that drunk sailor knows more...""",
 
    'exits': {},

    'items': [],

    'characters': []
}
room_pub = {
    'name': 'the Pub',

    'description': """An old western themed tavern with bar stools littered around the circle tables. A pool table in one corner
    next to a jukebox playing what sounds like the theme from 'The Good, the Bad and the Ugly'. There's a crowd of people watching
    a boxing match on the T.V., while one patron is passed out in a pool of his own sick... classy place, maybe the bar tender
    can tell me more about this place... """,

    'exits': {},

    'items': [],

    'characters': []
}
room_scrapheap = {
    'name': 'the scrapheap',

    'description': """There's a lot of scrap piles scattered around the yard. The owner must collect debris from 
    crashed vehicles and sell them to customers as there are many clients wandering around the yard looking for 
    spare parts. A large mechanical crusher is being operated at the end of the yard, crushing useless metals into
    useable materials.""",

    'exits': {},

    'items': [],

    'characters': []
}
room_hardware = {
    'name': 'the hardware store',

    'description': """A small store filled with items that may come in handy when repairing your ship, many other customers
     are talking to what appears to be the owner about something or other. There is a large scrap yard out the back with 
     all sorts of tools and spare parts lying about, maybe the owner or his engineers can help me fix the ship. """,

    'exits': {},

    'items': [],

    'characters': []
}
room_mayorhouse = {
    'name': 'the Mayors house',

    'description': """The mayor of the town's house, looks like he is paid very well. His house is enormous with lavish
    paintings of himself placed in pretty much every room, luxurious furniture everywhere... this man clearly has a lot of power
    and likes to look at himself... a lot.""",

    'exits': {},

    'items': [],

    'characters': []
}
room_cabin = {
    'name': 'the Cabin',

    'description':  """A hunter's cabin, fully decorated with trophies and hunting weapons from around the land. 
    A large stag's head is mounted above the fireplace, obviously the hunter's prize catch. There is a meaty smell radiating from the fire,
    the hunter must be cooking his latest catch. """,

    'exits': {},

    'items': [],

    'characters': []
}
room_caves = {
    'name': 'the Caves',

    'description': """The cave is narrow to start with but expands out into a large cavern area where a tribe of people
    are sat around a campfire cooking and chatting. The cave lights up as rays of sunshine enter the dark hole, illuminating
    several tunnels that appear to have been blocked off. A strange smell is radiating from the centre of the camp, 
    the Tribe must be cooking some exotic meal.""",

    'exits': {},

    'items': [],

    'characters': []
}
room_beach = {
    'name': 'the Beach',

    'description': """Golden sand and irregular bunches of sea weed lay on the beach extending as far as the eye can see, 
stopping at what looks like a small cliff with an old lighthouse, on the other side lies a wrecked old and 
rusty fish boat that hasn't been used for a long time. The fisherman stands proud beside his boat; legs wobbly 
whilst drinking the last drops from an old bottle, frequently mumbling and shouting about his rum and his boat.
A very distinct fish and rum stench comes from him...""", 

    'exits': {},

    'items': [],

    'characters': []
}
room_town = {
    'name': 'the Town',

    'description': """The town is quiet and peaceful, mostly residential with a few shops along the road just opposite from the 
extenuated beach. A fish & chip shop is one of the most popular shops around with a queue as long as 2 shops. Most 
other shops have closed for the day since it's a Sunday. Strangely enough, the hardware store and the bar are open 
and the Mayor is very open to home visits. At the moment, the Mayor is in his house. Everyone else is busy enjoying
the sun and are playing on the beach""", 

    'exits': {},

    'items': [],

    'characters': []
}
room_forest = {
    'name': 'the Forest',

    'description': """It's dark, raining and humid, in the distance you can hear the rustle of trees, crickets and various 
other animals. Subtle gushing sounds are sometimes heard. Haunting shadows cast over the forest from the 
dancing fire surrounding the spaceship. An infused stench of hair and skin surrounds the spaceship. Looking 
around you, not much is visible. You can hardly see anything. Many rocks and shrubs surround you.""", 

    'exits': {},

    'items': [],

    'characters': []
}
room_spaceship = {
    'name': 'the Spaceship',

    'description': """NASA sent you on a mission to test out their new levitation device. You reached the outer-atmosphere 
but the fuel tank exploded causing the spaceship to spin out of control back to Earth. You and your 
team tried emergency procedures on re-entry but most of the procedures failed, leaving your spaceship 
hurtling to an unknown island. Luckily a backup parachute was deployed late and helped slow the speed 
enough to prevent obliteration. The impact created a giant hole in the side of the spaceship, equipment 
is on fire and the injuries are critical. The engineer has a compound fracture of his fibula cutting 
off blood supply to his foot (amputation might be necessary), the pilot has a blown pupil from a brain 
injury causing intracranial pressure. The scientist has a dislocated shoulder and has sustained second 
degree burns and you were unconscious for a while, you're not sure how long but you think you're fine...

You need to move everyone to a safe place and repair the spaceship so you can call for help and if 
possible, pinpoint your location and fly back.""",

    'exits': {'outside': room_forest['name']},

    'items': [],

    'characters': []}
#Add the rooms to the list, for simplicity, we use names of the rooms themselves instead of remembering our own made-up ones
rooms = {
    room_spaceship['name']: room_spaceship,
    room_forest['name']: room_forest,
    room_caves['name']: room_caves,
    room_cabin['name']: room_cabin,
    room_town['name']: room_town,
    room_beach['name']: room_beach,
    room_shipwreck['name']: room_shipwreck,
    room_pub['name']: room_pub,
    room_hardware['name']: room_hardware,
    room_mayorhouse['name']: room_mayorhouse,
    room_mountain['name']: room_mountain}
#Add the certain items we want in our inventory
player.inventory = [item_torch]
#Let's add the current room to load up
player.current_room = rooms[room_spaceship['name']]
