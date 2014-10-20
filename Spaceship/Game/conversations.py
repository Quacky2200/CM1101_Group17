def testaction():
	print('rain drops keep falling my head')
test1 = ['Hello','What do you want?']
test2 = ['What\'s up?', ['Go away!']]
test3 = ['Bye!', testaction]
test_convo = [test1, test2, test3]
person = 'Bob'

conversation_tribe = []

conversation_mayor = []

conversation_hunter = []

conversation_hunter_mountain = []

conversation_hunter_attack = []

convo_me = True
def talkto(person, convolist):
	global convo_me
	if convo_me:
		for i in range(len(convolist)):
			print(str(i + 1) + ': ' + convolist[i][0])
		number_chosen = input('What do you want to say?\n> ')
		if not type(number_chosen) == int:
			print('Error, try again.')
			talkto(person, convolist)
		else:
			print('I say: ' + convolist[number_chosen - 1][0])
			convo_me = False
			talkto(person, convolist[number_chosen - 1][1])
	else:
		if len(convolist) == 2:
			if type(convolist) == str:
				print(person + ' says: ' + convolist)
			elif type(convolist) == list:
				print('There\'s more!')
				print(person + ' says: ' + convolist[0])
				talkto(person, convolist[1])
			elif callable(convolist[0]):
				print('Executable here')
				convolist()
print('Talking with ' + person)
talkto(person, test_convo)

