# Aaliya Hussain
# 2nd Period
# 1/24/20

import sys

def over(board):
    for sh in range(3):
        if board[sh*3] != "." and board[sh*3] == board[sh*3+1] == board[sh*3+2]:
            return True, board[sh*3]
    for sv in range(3):
        if board[sv] != "." and board[sv] == board[sv+3] == board[sv+6]:
            return True, board[sv]
    if board[0] != "." and board[0] == board[4] == board[8]:
        return True, board[0]
    if board[2] != "." and board[2] == board[4] == board[6]:
        return True, board[2]
    if "." not in board:
        return True, "tie"
    return False, ""

def possible(board):
    moves = []
    for i in range(9):
        if board[i] == ".":
            moves.append(i)
    return moves

# NEGAMAX
def negamax(board, player):
    # Computes the "negative" of the current player
    if player == "X":
        opp = "O"
    else:
        opp = "X"
    # Checks if the game is over
    pe = over(board)
    if pe[0]:
        if pe[1] == player:
            return 1, opp
        if pe[1] == opp:
            return -1, opp
        else:
            return 0, opp
    # If the game is still running, continue by calling negamax with the "negative" of the player
    cur_m = -2
    vars = possible(board)
    for vals in vars:
        nb = mm(board, vals, player)
        # Evaluate the max of the "negative" of the values returned by negamax
        m_poss = -1*negamax(nb, opp)[0]
        if m_poss > cur_m:
            cur_m = m_poss
    return cur_m, opp

def mm(board, pos, player):
    nb = list(board)
    nb[pos] = player
    return "".join(nb)

def pb(board):
    print("Current board:")
    print(board[:3], "\t","012")
    print(board[3:6], "\t", "345")
    print(board[6:], "\t", "678")

def np(board):
    xs = 0
    os = 0
    for i in board:
        if i == "X":
            xs += 1
        if i == "O":
            os += 1
    if xs > os:
        return "O"
    return "X"


# Game running
cb = sys.argv[1]
com = "X"
you = "O"
bm = -1
if cb == ".........":
    com = input("Should I be X or O?")
    print()
    pb(cb)
    print()
    if com == "O":
        you = "X"
        pm = possible(cb)
        print("You can move to any of these spaces: %s." % str(pm)[1:-1])
        ym = int(input("Your choice?"))
        print()
        cb = mm(cb, ym, "X")
        pb(cb)
        print()
else:
    pb(cb)
    print()
    n = np(cb)
    if n != "X":
        com = n
        you = "X"
while not over(cb)[0]:
    pm = possible(cb)
    bo = -2
    for p in pm:
        cbc = mm(cb, p, com)
        r = -negamax(cbc, you)[0]
        if r == 1:
            print("Moving at %s results in a win." % p)
        if r == -1:
            print("Moving at %s results in a loss." % p)
        if r == 0:
            print("Moving at %s results in a tie." % p)
        if r > bo:
            bo = r
            bm = p
    print()
    print("I choose space %s." % bm)
    cb = mm(cb, bm, com)
    print()
    pb(cb)
    print()
    o = over(cb)
    if o[0]:
        break
    pm = possible(cb)
    print("You can move to any of these spaces: %s." % str(pm)[1:-1])
    ym = int(input("Your choice?"))
    print()
    cb = mm(cb, ym, you)
    pb(cb)
    print()
o = over(cb)
if o[1] == com:
    print("I win!")
if o[1] == you:
    print("You win!")
if o[1] == "tie":
    print("We tied!")
