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
item_beer = {
    'id': 'beer',

    'name': 'a bottle of beer',

    'description':'a frothy alcoholic beverage',

    'weight': '500G',

    'enabled': [take, drop, use, give]

    }
item_pepper = {
    'id': 'pepper',

    'name': 'a bottle of Dr Pepper',

    'description':'a non-alcoholic fizzy drink',

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

    'description': 'Low battery - Off',

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

    'items': [item_fuelcanister]
    }
character_hunter = {
    'name': 'Rodney',

    'description': 'Proud of his wooden cabin and all the animals he has killed',

    'items': [item_boots]
    }
character_tribe = {
    'name': 'Chief Powhatan',

    'description': 'An angry leader of the tribe, always taking advantage of the general public',

    'items': []
    }
character_barman = {
    'name': 'Barman',

    'description': 'Loves local gossip and gives bad relationship advice.',

    'items': [item_rum]
    }
character_manager = {
    'name': 'Manager',

    'description': 'Handles customer requests. In his spare time, plays golf.',

    'items': []
}
#Rooms now need to be added (least important - children first)
room_blindlydark = {
    'name': 'explore',

    'description': 'You stumble, fall and then feel helpless without light. You return to the forest...', 'exits':{}, 'items':[], 'characters':[]
}
room_mountain = {
    'name': 'the Mountains',

    'description': """The mountain spans for miles around you, high snow-covered peaks surround a small camp where 
the Tribes' people are hiding. Large pens are visible, clearly herding mountain goats 
and other animals for the Tribes people to use in their day to day lives. A leader of
the group comes up to you and expects something in return for the care they have given
to your crew. You cannot leave without your crew.""", 'exits': {}, 'items': [], 'characters': [character_tribe]
    }
room_shipwreck = {
    'name': 'the shipwreck',

    'description': """An old looking ship that must have come aground during a storm. The whole ship is rotting 
away in the sand, making the name impossible to read. This is a sad sight, maybe that 
drunk sailor knows more...""", 'exits': {}, 'items': [], 'characters': [character_sailor]
    }
room_pub = {
    'name': 'the Pub',

    'description': """An old western themed tavern with bar stools littered around the circle tables. A pool table in one corner
next to a jukebox playing what sounds like the theme from 'The Good, the Bad and the Ugly'. 
There's a crowd of people watching a boxing match on the T.V., while one patron is passed 
out in a pool of his own sick... classy place, maybe the bar tender can tell me more about 
this place... """, 'exits': {}, 'items': [], 'characters': [character_barman]
    }
room_scrapheap = {
    'name': 'the scrapheap',

    'description': """There's a lot of scrap piles scattered around the yard. The owner 
must collect debris from crashed vehicles and sell them to customers as there are many 
clients wandering around the yard looking for spare parts. A large mechanical crusher is
being operated at the end of the yard, crushing useless metals into useable materials.""", 'exits': {}, 'items': [item_fueltank, item_scrapmetal], 'characters': []
    }
room_hardware = {
    'name': 'the hardware store',

    'description': """A small store filled with items that may come in handy when repairing your ship, many other customers
are talking to what appears to be the owner about something or other. There is a large 
scrap yard out the back with all sorts of tools and spare parts lying about, maybe the 
owner or his engineers can help me fix the ship. """, 'exits': {'north': room_scrapheap['name']}, 'items': [item_rivetgun], 'characters': [character_manager]
    }
room_mayorhouse = {
    'name': 'the Mayors house',

    'description': """The mayor of the town's house, looks like he is paid very well. His house is enormous with lavish
paintings of himself placed in pretty much every room, luxurious furniture everywhere... 
this man clearly has a lot of power and likes to look at himself... a lot.""", 'exits': {}, 'items': [], 'characters': [character_mayor]
    }
room_cabin = {
    'name': 'the Cabin',

    'description':  """A hunter's cabin, fully decorated with trophies and hunting weapons from around the land. 
A large stag's head is mounted above the fireplace, obviously the hunter's prize catch. 
There is a meaty smell radiating from the fire, the hunter must be cooking his latest 
catch. The crackle of the fire along with the warmth makes you feel safe. You eat dinner 
and fall asleep on the sofa. It was a good night.""", 'exits': {}, 'items': [], 'characters': [character_hunter]
    }
room_caves = {
    'name': 'the Caves',
    'description': """You were able to move all of your crew to the entrance of the cave 
where a tribe of people are sitting around a campfire; cooking and chatting. The cave lights 
up from the firelight and moonlight. Everything feels comfortably warm, natural and harmonious. 
A few of them start helping your wounded crew. You feel certain that they will be protected and 
recover well, and that you will be able to start repairing the spaceship.""",
#     'description': """The cave is narrow to start with but expands out into a large cavern area where a tribe of people
# are sat around a campfire cooking and chatting. The cave lights up as rays of sunshine enter the dark hole, illuminating
# several tunnels that appear to have been blocked off. A strange smell is radiating from the centre of the camp, 
# the Tribe must be cooking some exotic meal.""",
 'exits': {}, 'items': [], 'characters': []
    }
room_beach = {
    'name': 'the Beach',

    'description': """Golden sand and irregular bunches of sea weed lay on the beach extending as far as the eye can see, 
stopping at what looks like a small cliff with an old lighthouse, on the other side lies a wrecked old and 
rusty fish boat that hasn't been used for a long time. The fisherman stands proud beside his boat; legs wobbly 
whilst drinking the last drops from an old bottle, frequently mumbling and shouting about his rum and his boat.
A very distinct fish and rum stench comes from him...""", 'exits': {'inside':room_shipwreck['name']}, 'items': [], 'characters': []
    }
room_town = {
    'name': 'the Town',

    'description': """The town is quiet and peaceful, mostly residential with a few shops along the road just opposite from the 
extenuated beach. A fish & chip shop is one of the most popular shops around with a queue as long as 2 shops. Most 
other shops have closed for the day since it's a Sunday. Strangely enough, the hardware store and the bar are open 
and the Mayor is very open to home visits. At the moment, the Mayor is in his house. Everyone else is busy enjoying
the sun and are playing on the beach""", 'exits': {'north':room_hardware['name'], 'west': room_pub['name'], 'south': room_mayorhouse['name']}, 'items': [], 'characters': []
    }
room_forest = {
    'name': 'the Forest',

    'description': """It's dark, raining and humid, in the distance you can hear the rustle of trees, crickets and various 
other animals. Subtle gushing sounds are sometimes heard. Haunting shadows cast over the forest from the 
dancing fire surrounding the spaceship. An infused stench of hair and skin surrounds the spaceship. Looking 
around you, not much is visible. You can hardly see anything. Many rocks and shrubs surround you.""", 

    'exits': {'north':room_blindlydark['name'], 'east': room_blindlydark['name'], 'south':room_blindlydark['name'], 'west':room_blindlydark['name']}, 'items': [], 'characters': []
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
rooms = {}
def SyncRooms():
    for variable in globals():
        if 'room_' in variable and not variable in rooms:
            rooms[globals()[variable]['name']] = globals()[variable]
SyncRooms()
#Add the certain items we want in our inventory
player.inventory = [item_torch]
#Let's add the current room to load up
player.current_room = room_spaceship
