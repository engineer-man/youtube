# author: marmitegeek

import random as r
import math as m

print('This program runs the monty hall problem 100,000 times on each execution.')
print('The following is the number of times (as a percentage) the contestant wins or loses when switching their choice.')
print('Note: percentages are floored to remove the decimal places.')

win = 0
loss = 0

for i in range(100000):
	doors = [
		{'ID':1,'prize':'','selected':0,'open':0},
		{'ID':2,'prize':'','selected':0,'open':0},
		{'ID':3,'prize':'','selected':0,'open':0}
	]
	prizes = ['Goat','Goat','Car']

	doors[0]['prize'] = prizes[r.randint(0,2)]
	prizes.remove(doors[0]['prize'])
	#print('Door 1: ' + doors[0]['prize'])

	doors[1]['prize'] = prizes[r.randint(0,1)]
	prizes.remove(doors[1]['prize'])
	#print('Door 2: ' + doors[1]['prize'])

	doors[2]['prize'] = prizes[0]
	#print('Door 3: ' + doors[2]['prize'])

	contestant = r.randint(1,3)
	doors[contestant-1]['selected'] = 1
	#print('Contestant selects Door ' + str(contestant))

	monty = 0
	for d in doors:
		if d['prize'] == 'Goat' and d['selected'] == 0 and monty == 0:
			d['open'] = 1
			monty = d['ID']
	#print('Monty opens Door ' + str(monty))

	contestant = 0
	for d in doors:
		if d['selected'] == 0 and d['open'] == 0 and contestant == 0:
			d['selected'] = 1
			contestant = d['ID']
		if d['selected'] == 1 and d['ID'] != contestant:
			d['selected'] = 0
	#print('Contestant switches selection to Door ' + str(contestant))

	if doors[contestant-1]['prize'] == 'Car':
		win += 1
		#print('WIN')
	else:
		loss += 1
		#print('LOSS')
p_win = m.floor((win/100000)*100)
p_loss = m.floor((loss/100000)*100)

print('WINS: ' + str(p_win) + '%')
print('LOSS: ' + str(p_loss) + '%')
