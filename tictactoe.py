#importning:
import random
# universal variables:
# list of all positions on the board:
moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
# list of possible corner moves
corners = [moves[0], moves[2], moves[6], moves[8]]
# list of possible corners and center moves
corncen = [moves[4], moves[0], moves[2], moves[6], moves[8]]
# list of possible side moves
sides = [moves[1], moves[3], moves[5], moves[7]]



# Prints the board in a pretty format.
# Input: Board.
# Output: None.
def printBoard(b):
	for r in range(3):
		print "[", b[r][0], b[r][1], b[r][2], "]"



# Returns the other player.
# Input: Player "O" or "X".
# Output: Other player.
def otherPlayer(p):
	if p == "O":
		return "X"
	else:
		return "O"


# Detects whether a given player has won the game.
# Input: Board. Player "O" or "X".
# Output: Boolean.
def hasWon(board, player):
    for m in range(3):
        if board[m][0] == board[m][1] == board[m][2] == player != " ":
            return True
        elif board[0][m] == board[1][m] == board[2][m] == player != " ":
            return True
        elif board[0][0] == board[1][1] == board[2][2] == player != " ":
            return True
        elif board[0][2] == board[1][1] == board[2][0] == player != " ":
            return True
    return False




# Decides whether a player can win with one move.
# Input: board player "O" or "X"
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def maywin(board, player):
	# lists of the possible non-row wins on board:
	czero = [board[0][0], board[1][0], board[2][0]]
	cone = [board[0][1], board[1][1], board[2][1]]
	ctwo = [board[0][2], board[1][2], board[2][2]]
	dupdwn = [board[0][0], board[1][1], board[2][2]]
	ddwnup = [board[0][2], board[1][1], board[2][0]]

	for c in range(3):
		if board[c].count(player) == 2 and board[c].count(" ") == 1:
			return [c, board[c].index(" ")]
	if czero.count(player) == 2 and czero.count(" ") == 1:
		return [czero.index(" "), 0]
	elif cone.count(player) == 2 and cone.count(" ") == 1:
		return [cone.index(" "), 1]
	elif ctwo.count(player) == 2 and ctwo.count(" ") == 1:
		return [ctwo.index(" "), 2]
	elif dupdwn.count(player) == 2 and dupdwn.count(" ") == 1:
		l = [[0, 0], [1, 1], [2, 2]]
		return l[dupdwn.index(" ")]
	elif ddwnup.count(player) == 2 and ddwnup.count(" ") == 1:
		l = [[0, 2], [1, 1], [2, 0]]
		return l[ddwnup.index(" ")]
	else:
		return None


# Chooses a move at random from among the open sides on the board.  It attempts 10 possible randoms. It is possible, though imporobable, to generate only occupied spaces.
# Input: Board.
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def ranside(board):
	for x in range(10):
		r = random.choice(sides)
		if board[r[0]][r[1]] == " ":
			return r
	return None



# Chooses a move at random from among the open corners on the board.  It attempts 5 possible randoms. If there is more than one repeat, this means that it is possible not to generate unoccupied corner.
# Input: Board.
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def rancorner(board):
	for x in range(10):
		r = random.choice(corners)
		if board[r[0]][r[1]] == " ":
			return r
	return None


# Chooses a move at random from among the open center/corners on the board.  It attempts 5 possible randoms. If there is more than one repeat, this means that it is possible not to generate unoccupied corner.
# Input: Board.
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def rancorncen(board):
	for x in range(10):
		r = random.choice(corncen)
		if board[r[0]][r[1]] == " ":
			return r
	return None


# Selects the next move for the given player.
# Input: Board. Player "O" or "X" and the number of turns.
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def move(board, player, turns):
	rc = rancorner(board)
	rs = ranside(board)
	rcc = rancorncen(board)
	op = otherPlayer(player)
	# list of all corner positions one the board:
	bcorners = [board[0][0], board[0][2], board[2][0], board[2][2]]
	bsides = [board[0][1], board[1][0], board[1][2], board[2][1]]
	#Prints the current player
	print
	print player + "'s Turn: "#, turns + 1
	#Checks the board for a possible winning move and performs it if one exists.
	if maywin(board, player) != None:
		print "Winning play",
		return maywin(board, player)
	#Checks the board for a possible winning move for the otherPlayer and blocks it.
	elif maywin(board, op) != None:
		print "Block",
		return maywin(board, op)
	else:
	#diagrams of moves and qualifications as offensive and defensive assume that X starts and that even number "turns" (X) are offensive and odd number "turns" (O) are defensive.
		#first move
		if turns == 0:
			print "Corner/center play",
			return rcc
		#defensive move
		elif turns == 1 and board[1][1] == " ":
			print "Corner/center play",
			return rcc
		#offensive move providing these circumstances:
		#[X, , ]
		#[ ,O, ]
		#[ , ,X]
		elif turns == 2 and board [1][1] == op:
			print "Corner play",
			if board[0][0] == player:
				return [2, 2]
			elif board[0][2] == player:
				return [2, 0]
			elif board[2][0] == player:
				return [0, 2]
			elif board[2][2] == player:
				return [0, 0]
		#offensive move providing player with center and corner positions.
		elif turns == 2 and board[1][1] == player:
			print "Corner play",
			return rc
		#offensive move occupying center if not already occupied.
		elif turns >= 2 and board[1][1] == " ":
			return [1, 1]
		#defensive move
		elif turns == 3 and board[0][0] == board[2][2] == op:
			print "Side play",
			return rs
		#defensive move
		elif turns == 3 and board[0][2] == board[2][0] == op:
			print "Side play",
			return rs
		#offensive move allowing this win:
		#[X, ,X]
		#[ ,O, ]
		#[O, ,X]
		elif turns == 4 and board[0][0] == board[2][2] == player:
			print "Corner play",
			if board[0][2] == " ":
				return [0, 2]
			elif board[2][0] == " ":
				return [2, 0]
		#offensive move allowing this win:
		#[X, ,X]
		#[ ,O, ]
		#[O, ,X]
		elif turns == 4 and board[0][2] == board[2][0] == player:
			print "Corner play",
			if board[0][0] == " ":
				return [0, 0]
			elif board[2][2] == " ":
				return [2, 2]
		#offensive move allowing this win:
		#[X,X, ]
		#[O,X, ]
		#[ , ,O]
		elif turns == 4 and bcorners.count(player) == 1 and board[1][1] == player:
			if board[2][2] == player or board[0][2] == player and board[1][2] == " ":
				return [1, 2]
			if board[2][2] == player or board[2][0] == player and board[2][1] == " ":
				return [2, 1]
			if board[2][0] == player or board[0][0] == player and board[1][0] == " ":
				return [1, 0]
			if board[0][0] == player or board[0][2] == player and board[1][2] == " ":
				return [0, 1]
		#fill empty space if one exists on last turn.
		elif turns == 8:
			for x in range(3):
				if board[x].count(" ") == 1:
					print "Last play",
					return [x, board[x].index(" ")]
		#any other random move.
		else:
			if rc == None:
				print "Side play",
				return rs
			else:
				print "Corner play",
				return rc

# prints the winner of the game
# Inputs: board, player
# Outputs: prints Winner, or No winner.
def printWin(board, player):
	if hasWon(board, player) == True:
		print "Player ", player," has won!"
	elif hasWon(board, otherPlayer(player)):
		print "Player", otherPlayer(player),"has won!"
	else:
		print "Cat's game."


# Plays the computer against itself.
# Input: None.
# Output: None.
def computerVsComputer():
	# Initialize the game.
	board = [[" ", " " ," "], [" ", " " ," "], [" ", " " ," "]]
	player = "O"
	turns = 0
	printBoard(board)
	# Run the game.
	while turns < 9 and not hasWon(board, "X") and not hasWon(board, "O"):
		m = move(board, player, turns)
		if m == None or board[m[0]][m[1]] != " ":
		    print "Invalid move", m, "by player", player, "on this board:"
		    printBoard(board)
		    return
		board[m[0]][m[1]] = player
		print
		printBoard(board)
		player = otherPlayer(player)
		turns = turns + 1
	# Finish the game.
	printWin(board, player)

# If the user ran this file directly, then this code will be executed.
# If the user imported this file, then this code will not be executed.
if __name__ == "__main__":
	computerVsComputer()

#board = [["O", " " ," "], [" ", "X" ," "], ["X", " " ,"O"]]
#player = "X"
#m = maywin(board, player)
#printBoard(board)
#print r
#if m != None:
#	board[m[0]][m[1]] = player
#board[r[0]][r[1]] = player
#	printBoard(board)
#print m
