from story import *
import player
import random
from time import sleep
def give_map():
	if not item_map in player.inventory:
		player.inventory.append(item_map)
		print('Here\'s something for your troubles.\nYou have been given a Map!')
def sailor_give_money():
	if not item_money in player.inventory:
		player.inventory.append(item_money)
	elif item_money['description'] == '100 coins': print('You cannot hold anymore money')
	item_money['description'] = '100 coins'
	character_sailor['conversation'] = conversation_sailor_ask
def use_money(sellableitem, amount):
	for item in player.inventory:
		if item['id'] == item_money['id']:
			coins = int(item['description'].replace(' coins', ''))
			if (coins - amount) >= 0:
				item_money['description'] = str(coins - amount) + ' coins'
				print(character_barman['name'] + ' gives you some ' + sellableitem['id'])
				player.inventory.append(sellableitem)
			else:
				print('You need more money...')
				if (coins - amount) == 0: player.inventory.remove(item)
			return
	print('You don\'t have any money')
conversation_sailor_questions_unlocked = {
	'who': player.username,
	'output': [
		['I need help! My spaceship needs repairing can you help me?', {'who': character_sailor['name'],'output': ['Who do I look like? Your alien engineer?', give_map]}],
		['Do you know where I can get some tools?', {'who': character_sailor['name'], 'output':['You can find some at the hardware store in town.', give_map]}],
		['What happened to your boat?', {'who': character_sailor['name'], 'output':['I used to be great at fishing, I even had my own business but then that went down hill when \nI fell in love and then she left me. Now I just drink to get rid of the pain.', give_map]}],
		['Can I use parts of your boat?', {'who': character_sailor['name'], 'output':['Sorry, you can\'t have this beauty, find some metal somewhere else!', give_map]}]
	]
	}
def sailor_passed_unlock():
	character_sailor['conversation'] = conversation_sailor_questions_unlocked
	talk(character_sailor['conversation'])
def check_unlock_questions():
	if item_rum in player.inventory:
		player.inventory.remove(item_rum)
		talk({'who': character_sailor['name'], 'output': ['Yes man, thanks!', sailor_passed_unlock]})
	elif item_beer in player.inventory:
		talk({'who': character_sailor['name'], 'output': 'You idiot, I didn\'t want this!'})
	elif item_pepper in player.inventory:
		talk({'who': character_sailor['name'], 'output': 'You idiot, I\'m not a lightweight, yuck!'})
conversation_sailor_ask = {
	'who': character_sailor['name'],
	'output': ['Have you got it?', {
		'who': player.username,
		'output': [
			['Yes!', check_unlock_questions],
			['No?', {
				'who': character_sailor['name'],
				'output': ['What\'s wrong?', {
					'who': player.username,
					'output': [
						['I don\'t have any money!', sailor_give_money],
						['I just haven\'t got it', {
							'who': character_sailor['name'],
							'output': 'I can\'t help you then'
						}]
					]
				}]
			}]
		]
	}]
	}
def give_rum():
	use_money(item_rum, 10)
	if item_rum in player.inventory:
		character_sailor['conversation']['output']
def give_boots():
	if not item_boots in player.inventory: 
		player.inventory.append(item_boots)
		print('You recieve a pair of boots!')
def give_beer():
	#
	use_money(item_beer, 5)	
def give_fuelcanister():
	if not item_fuelcanister in player.inventory:
		player.inventory.append(item_fuelcanister)
		print('You were given a fuel canister, strangly enough, it has fuel inside it.')
		del character_mayor['conversation']['output'][1]['output'][1]['output'][1]['output'][0][1]['output'][1]['output'][3]
def give_pepper():
	#
	use_money(item_pepper, 4)
def repeat_barman():
	#
	talk(character_barman['conversation'])
def barman_offer_drink():
	#
	talk(character_barman['conversation']['output'][1]['output'][0][1])
def kicked_out_bar():
	print('You got kicked outside.')
	player.current_room = room_town
jokes = ['A bear walks into a bar and says to the bartender, ‘I’ll have a whisky and ……… soda.’ The bartender says, ‘Why the big pause?’ ‘Dunno,’ says the bear. ‘I’ve always had them.’', 
	'A grasshopper walks into a bar. The barman looks at him and says, ‘Did you know there’s a drink named after you?’ ‘Really?’ says the grasshopper. ‘There’s a drink called Jeremy?’', 
	'A dyslexic man walks into a bra...']
def play_joke():
	#
	print(jokes[random.randrange(0,len(jokes))])
def check_boots():
	if player.hole_replaced and player.fuel_tank_installed and player.fuel_installed:
		give_boots()
		room_mountain['exits']['south'] = room_caves['name']
	repeat_hunter()
conversation_barman = {
	'who': character_barman['name'],
	'output': ['Alright mate?', {
		'who': player.username,
		'output': [
			['Yeah!', {
				'who': character_barman['name'],
				'output': ['What\'s your posion?', {
					'who': player.username,
					'output': [
						['Apple juice', {
							'who': character_barman['name'],
							'output': ['Get out! Go on! GET OUT!', kicked_out_bar]
						}],
						['Rum', {
							'who': character_barman['name'],
							'output': give_rum
						}],
						['Beer', {
							'who': character_barman['name'],
							'output': give_beer
						}],
						['Dr Pepper', {
							'who': character_barman['name'],
							'output': give_pepper
						}]
					]
				}]
			}],
			['Can I have some advice?', {
				'who': character_barman['name'],
				'output': ['What type of advice you talkin\'?', {
					'who': player.username,
					'output': [
						['Relationship advice', {
							'who': character_barman['name'],
							'output': 'You\'re not gonna get anyone, next!'
						}],
						['I need to repair my spaceship and...', {
							'who': character_barman['name'],
							'output': 'I think you\'ve had to many beers alien guy...*chuckles* spaceship..'
						}],
						['Well...', {
							'who': character_barman['name'],
							'output': 'Let\'s not go there...'
						}]
					]
				}]
			}],
			['No',{
				'who': character_barman['name'],
				'output': ['Oh, well. That\'s too bad.', barman_offer_drink]
			}],
			['Tell me a joke',{
				'who': character_barman['name'],
				'output': ['*grumbles to himself*...OK then, prepare yourself!', {
					'who': player.username,
					'output': [
						['I\'m ready', {
							'who': character_barman['name'],
							'output': ['Here it goes...', play_joke]
						}],
						['I\'ve changed my mind', {
							'who': character_barman['name'],
							'output': '*grumbles to himself*'
						}]
					]
				}]
			}]
		]

	}]

	}
def repeat_hunter():
	talk(character_hunter['conversation'])
def unlock_town():
	del room_forest['exits']['west']
	room_forest['exits']['west'] = room_town['name']
	unlock_beach()
def unlock_beach():
	del room_forest['exits']['south']
	room_forest['exits']['south'] = room_beach['name']
	repeat_hunter()
conversation_hunter = {
	'who': player.username,
	'output': [
		['Do you have anything useful?', {
			'who': character_hunter['name'],
			'output': ["All I have are mountain boots for when I go hiking. Sorry.", check_boots]
		}],
		['I need some directions. Where are we?', {
			'who': character_hunter['name'],
			'output': ['The cave is to the east of the forest and the cabin is the north of the forest. Town can be found \nwest of the forest and the sea to the south', unlock_town]
		}],
		['Do you know how I can repair my spaceship?', {
			'who': character_hunter['name'],
			'output': ['I don\'t build spaceships so I don\'t know but a guy on the beach knows quite a bit about technology', unlock_beach]
		}],
		['Talk later', {
			'who': character_hunter['name'],
			'output': 'See you around!'
		}]
	]
	}
conversation_hunter_find_name = {
	'who': character_hunter['name'],
	'output': ['I\'m ' + character_hunter['name'] + ', Who are you?', {
		'who': player.username,
		'output': [
			["I'm " + player.username, {
				'who': character_hunter['name'],
				'output': ['Nice to meet you, ' + player.username + '. What are you doing in the forest?', conversation_hunter]
			}],
			["I'm a NASA astronaut, you should know who I am!", {
				'who': character_hunter['name'],
				'output': ['Wow that\'s awesome, why are you here?', conversation_hunter]
			}],
			["Your worst nightmare", {
				'who': character_hunter['name'],
				'output': ["*chuckles* Oh man, you do make me laugh!", conversation_hunter]
			}]
		]
	}]
	}
def find_hunter_name():
	room_blindlydark['description'] = 'You walk for a while but you feel lost so you return to the Forest'
	room_forest['exits']['north'] = room_cabin['name']
	character_hunter['conversation'] = conversation_hunter
	room_forest['description'] = 'The sunlight shines through the trees casting dusty light waves in parts of the forest; \nshowing what was once invisible. Insects and birds can be heard in the distance. \nThe stench has since dissipated.'
	room_spaceship['description'] = 'The spaceship that I crashed in, it\'s in a bad state and needs to be fixed \nbefore I can help my crewmates and call for help. Looks like I need a new \nfuel tank and some metal to fix this giant hole!'
	talk(conversation_hunter_find_name)
conversation_hunter_attack = {
	'who': 'Stranger',
	'output': ['You need to be careful! It\'s dangerous at night!', {
		'who': player.username,
		'output': [
			['Who are you?', find_hunter_name],
			['You nearly shot my head off!', {
				'who': 'Stranger',
				'output': ['Wow, wow, wow. I just saved you\'re life!', {
					'who': player.username,
					'output': [
						['but you could have...', {
							'who': 'Stranger',
							'output': ['I didn\'t though and you\'re alive so shut your ungrateful mouth before I shut it for you!', {
								'who':player.username, 
								'output':[
									['I\'m sorry!', {
										'who': 'Stranger',
										'output': ['No worries', {
											'who': player.username,
											'output': ['Who are you?', find_hunter_name]
										}]
									}],
									['Who are you?', find_hunter_name]
								]
							}]
						}],
						['I wouldn\'t trust you to shoot any gun at your age', {
							'who':player.username, 
							'output':['You\'re lucky to be alive. Try living without me here to protect the land! *polishes gun with breath*', {
								'who': player.username,
								'output': ['Who are you?', find_hunter_name]
							}] 
						}],
					]
				}]
			}],
			['Thank you!', {
				'who': 'Stranger',
				'output': ['Don\'t mention it!', {
					'who':player.username, 
					'output':['Who are you?', find_hunter_name]
				}]
			}],
			['Sorry Mr. know-it-all...', {
				'who': 'Stranger',
				'output': ['Just remember that I\'m the one carrying a shotgun, I could shoot you in a blast if I wanted so watch ya\' mouth!', {
					'who':player.username, 
					'output':[
						['I\'m sorry!', {
							'who': 'Stranger',
							'output': ['No worries', {
								'who': player.username,
								'output': ['Who are you?', find_hunter_name]
							}]
						}],
						['Who are you?', {
							'who': character_hunter['name'],
							'output': ['I\'m ' + character_hunter['name'] + ', Who are you?', find_hunter_name]
						}]
					]
				}]
			}]
		]
	}]
	}
conversation_sailor_rum = {
	'who': character_sailor['name'],
	'output': ['Help me out first and then I can help you!', {
		'who': player.username,
		'output': [
			['Sure!', {
				'who': character_sailor['name'],
				'output': ['I need a drink mate, I\'m desperate! I can\'t even think straight.', {
					'who': player.username,
					'output': [
						['Okay', {
							'who': character_sailor['name'],
							'output': ['Thanks so much! Here\'s some money!', sailor_give_money]
						}],
						['Why can\'t you just get it yourself?', {
							'who': character_sailor['name'],
							'output': ['I got barred from the pub...Here\'s some money, it won\'t take long!', sailor_give_money]
						}]
					]
				}]
			}],
			['No way!', {
				'who': character_sailor['name'],
				'output': 'I\'m afraid I can\'t help you then...'
			}]
		]
	}]
	}
conversation_sailor_questions = {
	'who': player.username,
	'output': [
		['I need help! My spaceship needs repairing can you help me?', {
			'who': character_sailor['name'],
			'output': 'Who do I look like? Your alien engineer?'
		}],
		['Do you know where I can get some tools?', conversation_sailor_rum],
		['What happened to your boat?', conversation_sailor_rum],
		['Can I use parts of your boat?', conversation_sailor_rum]
	]
	}
conversation_sailor = {
	'who': character_sailor['name'],
	'output': ['I\'m not interested in whateva trash ya be sellin\'!', {
		'who': player.username,
		'output': [
			['I\'m no saleman, I\'m a NASA astronaut!', {
				'who': character_sailor['name'],
				'output': 'That\'s what they always say!'
			}],
			['Listen \'ere you drunk idiot!', {
				'who': character_sailor['name'],
				'output': ['That\'s harsh man!', conversation_sailor_questions]
			}],
			['You\'re not worth talking to!', {
				'who': character_sailor['name'],
				'output': '*grumbles to himself*'
			}]
		]
	}]
	}
conversation_tribe = {'who':character_tribe['name'], 'output': 'Pay for crew, no pay, no crew...'}
conversation_mayor = {
	'who': character_mayor['name'],
	'output': ['WELCOME ' + player.username.upper() + '! I hope your finding the town enjoyable!', {
		'who': player.username,
		'output': ['Why thank you Mayor!', {
			'who': character_mayor['name'],
			'output': ['Not at all, I wish EVERYONE a brilliant day! *jolly laugh* What brings you here?', {
				'who': player.username,
				'output': [
					['I need help finding something', {
						'who': character_mayor['name'],
						'output': ['Well, what do you need to find?', {
							'who': player.username,
							'output': [
								['Alcohol', {
									'who': character_mayor['name'],
									'output': 'The pub in the town can offer plenty of alcohol! Enjoy!'
								}],
								['Scrap Metal', {
									'who': character_mayor['name'],
									'output': 'The hardware store will probably have something you might find interesting'
								}],
								['Boots', {
									'who': character_mayor['name'],
									'output': 'You\'re wearing shoes, is that enough? Most shops are closed on sundays so you\'ll have to wait until tomorrow'
								}],
								['A fuel canister', {
									'who': character_mayor['name'],
									'output': ['I have one of those in my backyard, you know what? Considering you\'re so nice, I\'ll let you borrow it', give_fuelcanister]
								}]
							]
						}]
					}],
					['How long have you been Mayor?', {
						'who': character_mayor['name'],
						'output': 'Oh, only a few years and I\'m enjoying it! *jolly laugh*'
					}],
					['Have a good day, Mayor.', {
						'who': character_mayor['name'], 
						'output': 'A good day to you too! *jolly laugh*'
					}]
				]
			}]
		}]
	}]
	}
def manager_cash():
	print('Looks like the cash register won\'t work for a while')
conversation_manager = {
	'who': character_manager['name'],
	'output': ['How can I help you?', {
		'who': player.username,
		'output': [
			['I\'d like to buy something', {
				'who': character_manager['name'],
				'output': ['My cash register isn\'t working, wait a minute', manager_cash]
			}],
			['I\'d like to complain', {
				'who': character_manager['name'],
				'output': ['What do you want to comlain about?', {
					'who': player.username,
					'output': [
						['Your free hardware magazines, they\'re rubbish', {
							'who': character_manager['name'],
							'output': 'What\'d you expect? They\'re free!'
						}],
						['You\'re customer service is terrible', {
							'who': character_manager['name'],
							'output': 'I totally agree'
						}],
						['You', {
							'who': character_manager['name'], 
							'output': ['What about me?', {
								'who': player.username,
								'output': [
									['Your interest in pancakes is irratating', {
										'who': character_manager['name'],
										'output': 'I don\'t even like pancakes?!?!'
									}],
									['Your hardware store lacks...hardware', {
										'who': character_manager['name'],
										'output': 'How original...'
									}]
								]
							}]
						}],
						['Your prices are a rip-off', {
							'who': character_manager['name'],
							'output': ['Are you gonna buy something or not?', {
								'who': player.username,
								'output': [
									['Yes', {
										'who': character_manager['name'],
										'output': {
											'who': character_manager['name'],
											'output': 'Well hurry up then!'
										}
									}],
									['Perhaps', {
										'who': character_manager['name'],
										'output': 'Eugh. Stupid people these days, they always think the customer is right.'
									}],
									['No', {
										'who': character_manager['name'],
										'output': 'Get out then!'
									}]
								]
							}]
						}]
					]
				}]
			}],
			['Nothing', {
				'who': character_manager['name'],
				'output': '*wispers* Stupid people these days, should\'ve gone into law at Uni'
			}]
		]
	}]
	}
character_tribe['conversation'] = conversation_tribe
character_hunter['conversation'] = conversation_hunter_attack
character_mayor['conversation'] = conversation_mayor
character_barman['conversation'] = conversation_barman
character_sailor['conversation'] = conversation_sailor
character_manager['conversation'] = conversation_manager
def talk(conversation):
	#Only start chatting if we have a dictionary (with a name)
	if type(conversation) == dict and len(conversation) == 2:
		#If the output is an action
		if callable(conversation['output']):
			conversation['output']()
			return	#if the output is a list
		elif type(conversation['output']) == list:
			if callable(conversation['output'][1]):
				print('[' + conversation['who'] + ']: ' + conversation['output'][0] + '\n')
				conversation['output'][1]()
				return
			elif type(conversation['output'][1]) == dict:
				#Print what we say
				print('[' + conversation['who'] + ']: ' + conversation['output'][0])
				print('')
				#Move onto the next person (a dict)
				talk(conversation['output'][1])
				#Else if the output has a matrix (options)
			elif type(conversation['output'][1]) == list:
				i = 0
				#we show all the options
				print('[' + conversation['who'] +']: ')
				for option in conversation['output']:
					print(str(i + 1) + ': ' + option[0])
					i += 1
				#Make the use choose an option
				try:
					number = int(input('Choose an option (1-' + str(i) + '): '))
					print('')
					print('[' + conversation['who'] + ']: ' + conversation['output'][(number - 1)][0])
					print('')
					if callable(conversation['output'][(number - 1)][1]):
						conversation['output'][(number - 1)][1]()
					else:
						talk(conversation['output'][(number - 1)][1])
				except (KeyboardInterrupt, SystemExit):
					print('')
					print('')
					quit()
				except ValueError:
					print('\nInvalid option!\n')
					talk(conversation)
				except IndexError:
					print('No such option!')
					talk(conversation)
		elif type(conversation['output'] == str):
			#If the origional output is just a string then the conversation leads no where, we say our stuff and go...
			print('[' + conversation['who'] + ']: ' + conversation['output'])
			print('')
			return
	else:
		print(':[ He\'s dead jim!')
# conversation_test2 = {
# 	'who': 'me',
# 	'output': ['Howdy partner!', {
# 		'who':'Dan',
# 		'output': ['Heyyyyy!', {
# 			'who': 'me',
# 			'output': ['What\'s up?', {
# 				'who': 'Dan',
# 				'output': 'Not much!'
# 			}]
# 		}]
# 	}]
# }
# conversation_test = {
# 	'who': 'Pick food',
# 	'output': [
# 		['burger', {'who': 'Advice', 'output':'Go to McDonalds'}],
# 		['fries', {'who': 'Advice', 'output':'Go to a supermarket'}],
# 		['hot dog', {'who': 'Advice', 'output':'Go to America'}],
# 		['chicken', {'who': 'Advice', 'output':'Go to KFC'}]
# 	]
# }
