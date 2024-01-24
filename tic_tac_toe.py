# Variable Initialization
result = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
iterator = 0
first_move = "x"
winner = ""

# Initializing View
print("---------------- TIC TAC TOE ----------------")

# Printing Board
def printView(res):
	for idx, i in enumerate(res):
		a = ""
		for index, j in enumerate(i):
			if (j == -1):
				a += "     "
			elif j == "x":
				a += "  x  "
			elif j == "o":
				a += "  o  "
			if (index + 1 < len(i)):
				a += "|"
		print(a)
		if (idx + 1 < len(res)):
			print("-----------------")
printView(result)
# Checking if winner is found in a row
def checkRowWinner(board):
	for row in board:
		if -1 not in row and len(set(row)) == 1:
			return True
	return False

# Checking if winner is found in a column
def checkColumnWinner(board):
	for idx, row in enumerate(board):
		col = [board[0][idx], board[1][idx], board[2][idx]]
		if -1 not in col and len(set(col)) == 1:
			return True
	return False

# Checking if winner is found in diagonal column
def checkDiagonal(board):
	diagonal = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
	for row in diagonal:
		if -1 not in row and len(set(row)) == 1:
			return True
	return False

# Looping through until all moves are played or a user has won the game
while iterator < 9:
	if (iterator > 4 and checkRowWinner(result) or checkColumnWinner(result) or checkDiagonal(result)):
		winner = "o" if first_move == "x" else "x"
		iterator = 10
	else:
		data = input(first_move + "'s move: ")
		if (data.isnumeric() == False):
			print("Please enter a valid input")
		elif (int(data) < 1 or int(data) > 9):
			print("Please enter value between 1 - 9")
		elif (int(data) == 1):
			if (isinstance(result[0][0], int)):
				iterator += 1
				result[0][0] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 2):
			if (isinstance(result[0][1], int)):
				iterator += 1
				result[0][1] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 3):
			if (isinstance(result[0][2], int)):
				iterator += 1
				result[0][2] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 4):
			if (isinstance(result[1][0], int)):
				iterator += 1
				result[1][0] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 5):
			if (isinstance(result[1][1], int)):
				iterator += 1
				result[1][1] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 6):
			if (isinstance(result[1][2], int)):
				iterator += 1
				result[1][2] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 7):
			if (isinstance(result[2][0], int)):
				iterator += 1
				result[2][0] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 8):
			if (isinstance(result[2][1], int)):
				iterator += 1
				result[2][1] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")
		elif (int(data) == 9):
			if (isinstance(result[2][2], int)):
				iterator += 1
				result[2][2] = first_move
				printView(result)
				first_move = "o" if first_move == "x" else "x"
			else:
				print("This is already filled")

if (winner):
	print(winner + " won the game")
else:
	print("Game Draw")
