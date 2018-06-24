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
    for m in range(2):
        if board[m][0] == board[m][1] == board[m][2] == player != " ":
            return True
        elif board[0][m] == board[1][m] == board[2][m] == player != " ":
            return True
        elif board[0][0] == board[1][1] == board[2][2] == player != " ":
            return True
        elif board[0][2] == board[1][1] == board[2][0] == player != " ":
            return True
        else: return False
#Decides whether a given player will win with a given board.
def maywin(board, player):
    czero = [board[0][0], board[1][0], board[2][0]]
    cone = [board[0][1], board[1][1], board[2][1]]
    ctwo = [board[0][2], board[1][2], board[2][2]]
    cupdwn = [board[0][0], board[1][1], board[2][2]]
    cdwnup = [board[2][0], board[1][1], board[0][2]]
    for c in range(2):
        czero = [board[0][0], board[1][0], board[2][0]]
        cone = [board[0][1], board[1][1], board[2][1]]
        ctwo = [board[0][2], board[1][2], board[2][2]]
        if board[c].count(player) == 2 and board[c].count(" ") == 1:
            return [c,board[c].index(" ")]
        elif czero.count(player) == 2 and czero.count(" ") == 1:
            return
        else: return None
randommove(board)
    r = random.randint(
        if

# import random then: random.randint(3,11) "provides random integer between 3 and 11 including 3 and 11"

# Selects the next move for the given player.
# Input: Board. Player "O" or "X".
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def move(board, player):
    if turns == 0:
    	#option to return any corner position
        return [0, 0] or [0, 2] or [2, 0] or [2, 2]
    #if corner has been played, play opposite corner
    elif turns == 1 and board[0][2] == player:
        return [2, 0]
    elif turns == 1 and board[2][2] == player:
        return [0, 0]
    elif turns == 1 and board[2][0] == player:
        return [0, 2]
    elif turns == 1 and board[0][0] == player:
        return [2, 2]
    else:
    	return [0, 0]

    #elif board[0][2] == " ":
        #return [0, 2]
    #elif board[0][2] == " ":
       # return [0, 2]
    #elif board[0][2] == " ":
        #return [0, 2]
    #elif board[0][2] == " ":
        #return [0, 2]
    #else:
        #return None

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
	if hasWon(board, "O"):
		print "Player O has won!"
	elif hasWon(board, "X"):
		print "Player X has won!"
	else:
		print "Draw."

# If the user ran this file directly, then this code will be executed.
# If the user imported this file, then this code will not be executed.
#if __name__ == "__main__":
#	computerVsComputer()

board = [[" ", "X" ,"X"], [" ", "O" ," "], ["O", " " ,"X"]]
player = "X"
printBoard(board)
print maywin(board, player)

def test():
    board = [["O", "X" ,"X"], [" ", "O" ," "], ["O", " " ,"X"]]
    printBoard(board)
    player = "O"
    hasWon(board, player)
    if hasWon(board, "O"):
        print "Player O has won!"
    elif hasWon(board, "X"):
        print "Player X has won!"
    else:
        print "No winner."
