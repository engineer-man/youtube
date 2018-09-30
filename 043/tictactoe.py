import os

player=0
moves=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def ispace():
	for x in range(11):
		if x==3 or x==7:
			print('|',end='')

		else:
			print('  ',end='')

	print()


def inpspace(r,c):
	for x in range(3):
		if x==1:
			print(moves[r][c], '', end='')

		else:
			print('  ',end='')

	#print()


def iline():
	for x in range(11):
		if x==3 or x==7:
			print('|',end='')

		else:
			print('__',end='')

	print()


def board():
	os.system('clear')
	ispace()
	inpspace(0, 0)
	print('|', end='')
	inpspace(0, 1)
	print('|', end='')
	inpspace(0, 2)
	print()
	iline()
	ispace()
	inpspace(1, 0)
	print('|', end='')
	inpspace(1, 1)
	print('|', end='')
	inpspace(1, 2)
	print()
	iline()
	ispace()
	inpspace(2, 0)
	print('|', end='')
	inpspace(2, 1)
	print('|', end='')
	inpspace(2, 2)
	print()
	ispace()


def player1():
	print('Player 1\'s Turn:\n')
	def fun():
		r, c = int(input('Row :')) - 1, int(input('Column :')) - 1
		if (r>3 or c>3 or moves[r][c] == 'X' or moves[r][c] == 'O'):
			print('Invalid Input!! Please Try Again!!')
			fun()

		else:
			moves[r][c] = 'X'
			board()

	fun()

def player2():
	print('Player 2\'s Turn:\n')

	def fun():
		r, c = int(input('Row :')) - 1, int(input('Column :')) - 1
		if (r>3 or c>3 or moves[r][c] == 'X' or moves[r][c] == 'O'):
			print('Invalid Input!! Please Try Again!!')
			fun()

		else:
			moves[r][c] = 'O'
			board()

	fun()


def callplay():
	if (moves[0][0] == moves[0][1] == moves[0][2] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[1][0] == moves[1][1] == moves[1][2] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[2][0] == moves[2][1] == moves[2][2] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][0] == moves[1][0] == moves[2][0] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][1] == moves[1][1] == moves[2][1] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][2] == moves[1][2] == moves[2][2] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][0] == moves[1][1] == moves[2][2] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][2] == moves[1][1] == moves[2][0] == 'X'):

		player = 1
		print('Player ', player, ' won!')
		return 1

	if (moves[0][0] == moves[0][1] == moves[0][2] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[1][0] == moves[1][1] == moves[1][2] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[2][0] == moves[2][1] == moves[2][2] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][0] == moves[1][0] == moves[2][0] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][1] == moves[1][1] == moves[2][1] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][2] == moves[1][2] == moves[2][2] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][0] == moves[1][1] == moves[2][2] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1

	elif (moves[0][2] == moves[1][1] == moves[2][0] == 'O'):

		player = 2
		print('Player ', player, ' won!')
		return 1


def play():
	global player,moves
	steps=0
	while steps<4:
		player1()
		if callplay()==1:
			break

		player2()
		if callplay()==1:
			break

		steps+=1

	else:
		player1()
		if callplay() != 1:
			print('Game ended in a Tie!!')

	print('Play Again??')
	if(input("Press '1' for YES and any other key for EXIT!!")=='1'):
		moves = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		board()
		play()


def disp():
	print('Welcome To Tic-Tac-Toe Game!!')
	print('Player 1 will play as X')
	print('Player 2 will play as O')
	board()
	if input("Press '1' to play and any other key to exit!\n") != '1':
		exit()
	play()


disp()
