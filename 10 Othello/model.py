# Aaliya Hussain
# 2nd Period
# 12/19/19

import re
import random

start = "???????????........??........??........??...o@...??...@o...??........??........??........???????????"
dirs = ["hf", "hr", "vf", "vr", "lf", "lr", "rf", "rr"]
dchange = [1, -1, 10, -10, 11, -11, 9, -9]

def pb(board):
    for x in range(10):
        print(" ".join(board[x*10:x*10+10]))

def possMoves(board, token):
    ret = dict()
    if token == "@":
        ex = "^\.o+@"
    else:
        ex = "^\.@+o"
    for i in range(11, 89):
        if board[i] == ".":
            if nextToOpp(board, token, i):
                tc = tocheck(board, i)
                for it in range(len(tc)):
                    if re.search(ex, tc[it]) is not None:
                        if i not in ret:
                            ret[i] = tuple()
                        temp = list(ret[i])
                        temp.append(dirs[it])
                        ret[i] = tuple(temp)
    return ret

def nextToOpp(board, token, i):
    if token == "@":
        opp = "o"
    else:
        opp = "@"
    if board[i-10] == opp or board[i+10] == opp or board[i-1] == opp or board[i+1] == opp or board[i-9] == opp or board[i-11] == opp or board[i+11] == opp or board[i+9] == opp:
        return True
    return False

def tocheck(board, index):
    ret = []
    # Row
    row = int(index/10)
    ret.append(board[index:row*10+10])
    ret.append(board[index:row*10-1:-1])
    # Column
    col = index%10
    lcol = list(board[c] for c in range(index, 90+col+1, 10))
    ret.append("".join(lcol))
    lcol = list(board[c] for c in range(index, col-1, -10))
    ret.append("".join(lcol))
    # Lefthand diagonal
    ldstop = index
    while board[ldstop] != "?":
        ldstop += 11
    ldl = list(board[l] for l in range(index, ldstop+1, 11))
    ret.append("".join(ldl))
    ldstart = index
    while board[ldstart] != "?":
        ldstart -= 11
    ldl = list(board[l] for l in range(index, ldstart - 1, -11))
    ret.append("".join(ldl))
    # Righthand diagonal
    rdstop = index
    while board[rdstop] != "?":
        rdstop += 9
    ldr = list(board[r] for r in range(index, rdstop + 1, 9))
    ret.append("".join(ldr))
    rdstart = index
    while board[rdstart] != "?":
        rdstart -= 9
    ldr = list(board[r] for r in range(index, rdstart - 1, -9))
    ret.append("".join(ldr))
    return ret

def move(board, token, index, ds):
    if token == "@":
        opp = "o"
    else:
        opp = "@"
    bl = list(board)
    bl[index] = token
    for d in range(len(ds)):
        dind = dirs.index(ds[d])
        change = dchange[dind]
        pc = index
        while pc == index or bl[pc] != token:
            if bl[pc] == opp:
                bl[pc] = token
            pc += change
    nboard = "".join(bl)
    return nboard

def scores(board):
    print("White: %s" % board.count("o"))
    print("Black: %s" % board.count("@"))

def mrm(board, ms, token):
    r = random.choice(list(ms.keys()))
    print("Chose %s" % r)
    moves.append(r)
    nboard = move(board, token, r, ms[r])
    return nboard

moves = []
board = start
player = "@"
pn = "Black"
oge = 0
while oge <= 1 and "." in board:
    pb(board)
    scores(board)
    pm = possMoves(board, player)
    print("%s Possible Moves: %s" % (pn, sorted(list(pm.keys()))))
    if len(pm) != 0:
        board = mrm(board, pm, player)
        oge = 0
    else:
        moves.append(-1)
        print("Pass")
        oge += 1
    if player == "@":
        player = "o"
        pn = "White"
    else:
        player = "@"
        pn = "Black"
    print()
pb(board)
print("Percent White: %s" % (board.count("o")/64*100))
print("Percent Black: %s" % (board.count("@")/64*100))
print(moves)
