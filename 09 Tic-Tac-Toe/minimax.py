# Aaliya Hussain
# 2nd Period
# 12/10/19

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

def max(board):
    pe = over(board)
    if pe[0]:
        if pe[1] == "X":
            return 1
        if pe[1] == "O":
            return -1
        else:
            return 0
    vars = possible(board)
    m = -2
    for vals in vars:
        nb = mm(board, vals, "X")
        m2 = min(nb)
        if m2 > m:
            m = m2
    return m


def min(board):
    pe = over(board)
    if pe[0]:
        if pe[1] == "X":
            return 1
        if pe[1] == "O":
            return -1
        else:
            return 0
    vars = possible(board)
    m = 2
    for vals in vars:
        nb = mm(board, vals, "O")
        m2 = max(nb)
        if m2 < m:
            m = m2
    return m

def pb(board):
    print("Current board:")
    print(board[:3], "\t","012")
    print(board[3:6], "\t", "345")
    print(board[6:], "\t", "678")

def mm(board, pos, player):
    nb = list(board)
    nb[pos] = player
    return "".join(nb)

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

cb = sys.argv[1]
com = "X"
you = "O"
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
    if com == "X":
        bo = -2
    else:
        bo = 2
    for p in pm:
        cbc = mm(cb, p, com)
        if com == "X":
            r = min(cbc)
            if r == 1:
                print("Moving at %s results in a win." % p)
            if r == -1:
                print("Moving at %s results in a loss." % p)
            if r == 0:
                print("Moving at %s results in a tie." % p)
            if r > bo:
                bo = r
                bm = p
        else:
            r = max(cbc)
            if r == -1:
                print("Moving at %s results in a win." % p)
            if r == 1:
                print("Moving at %s results in a loss." % p)
            if r == 0:
                print("Moving at %s results in a tie." % p)
            if r < bo:
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
        if o[1] == com:
            print("I win!")
        if o[1] == you:
            print("You win!")
        if o[1] == "tie":
            print("We tied!")
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