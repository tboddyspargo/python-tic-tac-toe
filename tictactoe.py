#Tic-Tac-Toe AI created by Tyler BoddySpargo in the CS111 class of Spring 2012, instructed by Josh Davis.
import random

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




# Decides whether the player can win with one move.
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


# Randomely chooses a list of 2 integers from a list.
# Inputs: List
# Outputs: Pair of 0, 1, or 2, indicating space in which to move, or None.
def randmove(List):
    if len(List) != 0:
        return List[random.randint(0, len(List) - 1)]
    else:
        return None


# Creates a list of moves refering to all of the empty corner spaces.
# Input: board
# Output: List of pars of 0, 1, or 2, indicating space in which to move, even if it is empty.
def availcorn(board):
    L = []
    if board[0][0] == " ":
        L = L + [[0, 0]]
    if board[0][2] == " ":
        L = L + [[0, 2]]
    if board[2][0] == " ":
        L = L + [[2, 0]]
    if board[2][2] == " ":
        L = L + [[2, 2]]
    return L

# Creates a list of moves refering to all of the empty spaces on the board.
# Input: board
# Output: List of pars of 0, 1, or 2, indicating space in which to move, even if it is empty.
def avail(board):
    L = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                L = L + [[i, j]]
    return L

# Creates a list of moves refering to all of the empty corner/center spaces.
# Input: board
# Output: List of pars of 0, 1, or 2, indicating space in which to move, even if it is empty.
def availcorncen(board):
    L = []
    if board[0][0] == " ":
        L = L + [[0, 0]]
    if board[0][2] == " ":
        L = L + [[0, 2]]
    if board[2][0] == " ":
        L = L + [[2, 0]]
    if board[2][2] == " ":
        L = L + [[2, 2]]
    if board[1][1] == " ":
        L = L + [[1, 1]]
    return L

# Creates a list of moves refering to all of the empty side spaces.
# Input: board
# Output: List of pars of 0, 1, or 2, indicating space in which to move, even if it is empty.
def availside(board):
    L = []
    if board[0][1] == " ":
        L = L + [[0, 1]]
    if board[1][0] == " ":
        L = L + [[1, 0]]
    if board[1][2] == " ":
        L = L + [[1, 2]]
    if board[2][1] == " ":
        L = L + [[2, 1]]
    return L


# Selects the next move for the given player.
# Input: Board. Player "O" or "X" and the number of turns.
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def move(board, player):
	asd = availside(board)
	ac = availcorn(board)
	acc = availcorncen(board)
	ab = avail(board)
	op = otherPlayer(player)
	# The variable "turns" in computerVsComputer belongs to computerVsComputer(), thus it isn't useful here and if I play this AI against a human, turns will no longer register the same if I "imported" that variable anyways.  I have, as a result, provided this substitute that returns the current turn.
	turns = board[0].count(player) + board[1].count(player) + board[2].count(player) + board[0].count(op) + board[1].count(op) + board[2].count(op)
	# list of contents of all corner positions on the board:
	bcorners = [board[0][0], board[0][2], board[2][0], board[2][2]]
	# list of contents of all the side positions on the board:
	bsides = [board[0][1], board[1][0], board[1][2], board[2][1]]
	# lists of contents of all positions in the three collumns on the board:
	clo = [board[0][0], board[1][0], board[2][0]] # left collumn (one)
	clt = [board[0][1], board[1][1], board[2][1]] # left collumn (two)
	clth = [board[0][2], board[1][2], board[2][2]] # left collumn (three)
	#Prints the current player
	print
	print player + "'s Turn: ", turns
	#Checks the board for a possible winning move and returns it if one exists.
	if maywin(board, player) != None:
		#print "Winning play",
		return maywin(board, player)
	#Checks the board for a possible winning move for the otherPlayer and blocks it.
	elif maywin(board, op) != None:
		#print "Block",
		return maywin(board, op)
	else:
	#diagrams of moves and qualificationsas offensive and defensive show below assume that X starts and that even number "turns" (X) are offensive and odd number "turns" (O) are defensive.
		#first move is played at random
		if turns == 0:
			#print "Random play",
			return randmove(ab)
		#defensive move - fills middle space if otherPlayer occupies a side
		elif turns == 1 and board[1][1] == " " and bsides.count(op) == 1:
			#print "Center play",
			return [1, 1]
		#defensive move playing opposite player's corner position.
		elif turns == 1 and bcorners.count(op) == 1:
			#print "Corner/Center play",
			if board[0][0] == op:
				return random.choice([[2, 2], [1, 1]])
			elif board[0][2] == op:
				return random.choice([[2, 0], [1, 1]])
			elif board[2][0] == op:
				return random.choice([[0, 2], [1, 1]])
			elif board[2][2] == op:
				return random.choice([[0, 0], [1, 1]])
		#offensive move providing these circumstances (and variations on them):
		#[X, , ]
		#[ ,O, ]
		#[ , ,X]
		elif turns == 2 and board [1][1] == op and bcorners.count(player) == 1:
			#print "Corner play",
			if board[0][0] == player:
				return [2, 2]
			elif board[0][2] == player:
				return [2, 0]
			elif board[2][0] == player:
				return [0, 2]
			elif board[2][2] == player:
				return [0, 0]
		#offensive move profiding these circumstances (and variations on them):
		#[X, ,O]
		#[ , , ]
		#[ , ,X]
		elif turns == 2 and bcorners.count(" ") == 2 and board[0].count(" ") != board[2].count(" ") != clo.count(" ") != clth.count(" ") != 0:
			#print "Corner play",
			if board[0][0] == player:
				return [2, 2]
			elif board[0][2] == player:
				return [2, 0]
			elif board[2][0] == player:
				return [0, 2]
			elif board[2][2] == player:
				return [0, 0]
		# offensive move -providing these circumstances (and variations on them):
		#[ ,X, ]
		#[ ,X,O]
		#[ , , ]
		elif turns == 2 and board[1][1] == player and bsides.count(op) == 1:
			#print "Side play"
			if clt.count(op) == 1:
				return random.choice([[1, 0], [1, 2]])
			elif board[1].count(op) == 1:
				return random.choice([[0, 2], [2, 1]])
		# offensive move providing player with center and corner positions.
		elif turns == 2 and board[1][1] == player:
			#print "Corner play",
			return randmove(ac)
		# offensive move occupying center if not already occupied.
		elif turns >= 2 and board[1][1] == " ":
			#print "Center play",
			return [1, 1]
		# random defensive move
		elif turns == 3 and board[0][0] == board[2][2] == op:
			#print "Side play",
			return randmove(asd)
		# random defensive move
		elif turns == 3 and board[0][2] == board[2][0] == op:
			#print "Side play",
			return randmove(asd)
		#defensive move blocking future possible win and providing these circumstances:
		#[ ,X,O]
		#[ ,O,X]
		#[ , , ]
		elif turns == 3 and board[1][1] == player and bsides.count(op) == 2:
			#print "Side play",
			if clth.count(op) == 1 and board[2].count(op) == 1:
				return [2, 2]
			elif clth.count(op) == 1 and board[0].count(op) == 1:
				return [1, 2]
			elif clo.count(op) == 1 and board[0].count(op) == 1:
				return [0, 0]
			elif clo.count(op) == 1 and board[2].count(op) == 1:
				return [2, 0]
			else:
				return randmove(asd)
		#defensive move blocking future possible win and providing these circumstances:
		#[ ,X,O]
		#[ ,O, ]
		#[ , ,X]
		elif turns == 3 and board[1][1] == player and bsides.count(op) == bcorners.count(op) == 1:
			#print "Corner play",
			if board[0].count(op) == board[1].count(op) == 1:
				if board[0][0] == " ":
					return [0, 0]
				if board[0][2] == " ":
					return [0, 2]
			if board[1].count(op) == board[2].count(op) == 1:
				if board[2][0] == " ":
					return [2, 0]
				if board[2][2] == " ":
					return [2, 2]
			if clo.count(op) == clt.count(op) == 1:
				if board[0][0] == " ":
					return [0, 0]
				if board[2][0] == " ":
					return [2, 0]
			if clt.count(op) == clth.count(op) == 1:
				if board[0][2] == " ":
					return [0, 2]
				if board[2][2] == " ":
					return [2, 2]
		#offensive move providing this win:
		#[X,X, ]
		#[O,X, ]
		#[ , ,O]
		## this long if statement checks to see that: 1) player ocupies the center and one corner space 2) the otherPlayer occupies one side and one corner space on the board 3) the two places occupied by otherPlayer are neither in the same row nor in the same collumn, 4) Then places player in the appropriate place to provide the win.
		elif turns == 4 and board[1][1] == player and bsides.count(op) == bcorners.count(op) == bcorners.count(player) == 1 and board[0].count(op) <= 1 and board[1].count(op) <= 1 and board[2].count(op) <= 1 and clo.count(op) <= 1 and clt.count(op) <= 1 and clth.count(op) <= 1:
			#print "Side play",
			if bcorners.index(op) == 0:
				return [1, 2]
			elif bcorners.index(op) == 1:
				return [2, 1]
			elif bcorners.index(op) == 2:
				return [0, 1]
			elif bcorners.index(op) == 3:
				return [1, 0]
		elif turns == 4 and board[0].count(player) <= 1 and board[1].count(player) <= 1 and board[2].count(player) <= 1 and clo.count(player) <= 1 and clt.count(player) <= 1 and clth.count(player) <= 1:
			#print "Corner play",
			if board[1].count(" ") == 0 and board[1][0] == board[0][2] == player:
				return [0, 0]
			elif board[1].count(" ") == 0 and board[1][0] == board[2][2] == player:
				return [2, 0]
			elif board[1].count(" ") == 0 and board[1][2] == board[0][0] == player:
				return [0, 2]
			elif board[1].count(" ") == 0 and board[1][2] == board[2][0] == player:
				return [2, 2]
			elif clt.count(" ") == 0 and board[0][1] == board[2][2] == player:
				return [0, 2]
			elif clt.count(" ") == 0 and board[0][1] == board[2][0] == player:
				return [0, 0]
			elif clt.count(" ") == 0 and board[2][1] == board[0][0] == player:
				return [2, 0]
			elif clt.count(" ") == 0 and board[2][1] == board[0][2] == player:
				return [2, 2]
		#offensive move providing this win (and it's variations):
		#[ ,X,X]
		#[O,X, ]
		#[ ,O, ]
		elif turns == 4 and board[1][1] == player and bsides.count(op) == 2 and bsides.count(player) == 1:
			#print "Corner play",
			if board[0].count(player) == 1:
				return random.choice([[0, 0], [0, 2]])
			elif clo.count(player) == 1:
				return random.choice([[0, 0], [2, 0]])
			elif clth.count(player) == 1:
				return random.choice([[2, 2], [0, 2]])
			elif board[2].count(player) == 1:
				return random.choice([[2, 2], [2, 0]])
		#offensive move allowing this win:
		#[X, ,X]
		#[ ,O, ]
		#[O, ,X]
		# This long if statement checks that: 1) player occupies 2 corner spaces that are opposite eachother and 2) otherPlayer occupies one corner space and the middle space.
		elif turns == 4 and bcorners.count(player) == 2 and bcorners.count(op) == 1 and board[1][1] == op:
			#print "Corner play",
			return randmove(ac)
		elif turns == 5 and board[1][1] == player and bsides.count(op) == 3 and bsides.count(player) == 1:
			#print "Corner play",
			if bsides.index(player) == 0:
				return [0, 0]
			elif bsides.index(player) == 1:
				return [0, 0]
			elif bsides.index(player) == 2:
				return [2, 2]
			elif bsides.index(player) == 3:
				return [2, 2]
		#fill empty space if one exists on last turn.
		elif turns == 8:
			#print "Last play",
			for x in range(3):
				if board[x].count(" ") == 1:
					return [x, board[x].index(" ")]
		#any other random move.
		else:
			if randmove(ac) == None:
				#print "Side play",
				return randmove(asd)
			else:
				#print "Corner play",
				return randmove(ac)

# prints the winner of the game
# Inputs: board, player, "X" or "O"
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
		m = move(board, player)
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

# Plays the game n number of times
#if __name__ == "__main__":
#	n = 1000
#	for i in range(n):
#		print "Game", n
#		computerVsComputer()
#		print
#		print
