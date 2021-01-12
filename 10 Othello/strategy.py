# Aaliya Hussain
# 2nd Period
# 1/22/20

import time
import re

dirs = ["hf", "hr", "vf", "vr", "lf", "lr", "rf", "rr"]
dchange = [1, -1, 10, -10, 11, -11, 9, -9]
corners = [11, 18, 81, 88]
weak = [(12, 21, 22), (17, 28, 27), (71, 82, 72), (87, 78, 77)]
opp = "o"


class Strategy():
    def best_strategy(self, board, token, best_move, still_running):
        global opp
        time.sleep(1)
        d = 0
        moves = 1
        if token != "@":
            opp = "@"
        while still_running.value:
            best = -10000000000
            choices = possMoves(board, token)[0]
            for ch in choices.keys():
                if best == -10000000000:
                    best_move.value = ch
                nb = move(board, token, ch, choices[ch])
                e = min(token, opp, nb, moves+1, d, -10000000000, 10000000000)
                if e > best:
                    best = e
                    best_move.value = ch
            d += 1
        moves += 2

def min(token, opp, board, moves, depth, alpha, beta):
    if depth == 0:
        return heur(board, moves, token, opp)
    choices = possMoves(board, opp)[0]
    if len(choices) == 0:
        return heur(board, moves, token, opp)
    cmin = 10000000000
    for m in choices.keys():
        new = move(board, opp,  m, choices[m])
        comp = max(token, opp, new, moves+1, depth-1, alpha, beta)
        if comp < cmin:
            cmin = comp
        if comp < beta:
            beta = comp
        if alpha >= beta: #PRUNING
            break
    return cmin

def max(token, opp, board, moves, depth, alpha, beta):
    if depth == 0:
        return heur(board, moves, token, opp)
    choices = possMoves(board, token)[0]
    if len(choices) == 0:
        return heur(board, moves, token, opp)
    cmax = -10000000000
    for m in choices.keys():
        new = move(board, token,  m, choices[m])
        comp = min(token, opp, new, moves+1, depth-1, alpha, beta)
        if comp > cmax:
            cmax = comp
        if comp > alpha:
            alpha = comp
        if alpha >= beta: #PRUNING
            break
    return cmax

def possMoves(board, token):
    ret = dict()
    pot = 0
    if token == "@":
        ex = "^\.o+@"
    else:
        ex = "^\.@+o"
    for i in range(11, 89):
        if board[i] == ".":
            if nextToOpp(board, token, i):
                pot += 1
                tc = tocheck(board, i)
                for it in range(len(tc)):
                    if re.search(ex, tc[it]) is not None:
                        if i not in ret:
                            ret[i] = tuple()
                        temp = list(ret[i])
                        temp.append(dirs[it])
                        ret[i] = tuple(temp)
    return ret, pot

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

def heur(board, moves, token, opp):
    global corners
    if moves < 57:
        # Mobility
        mob = potmob(board, token, opp)
        # Corners
        mcor = 0
        ocor = 0
        mstab = 0
        ostab = 0
        for i in range(len(corners)):
            if board[corners[i]] == token:
                mcor += 1
                mstab += 5
                for i2 in range(3):
                    if board[weak[i][i2]] == token:
                        mstab += 1
            else:
                for i2 in range(3):
                    if board[weak[i][i2]] == token:
                        mstab -= 4
                        if i2 == 2:
                            mstab -= -1
            if board[corners[i]] == opp:
                ocor += 1
                ostab += 5
                for i2 in range(3):
                    if board[weak[i][i2]] == opp:
                        ostab += 1
            else:
                for i2 in range(3):
                    if board[weak[i][i2]] == opp:
                        ostab -= 4
                        if i2 == 2:
                            ostab -= -1
        corn = mcor-ocor
        # Stability
        stab = mstab-ostab
        if moves <= 17:
            return 2*(mob[0]-mob[1])+10*corn+4*stab
        else:
            return (mob[0]-mob[1])+15*corn+6*stab
    else:
        score = 0
        for i in range(11, 89):
            if board[i] == token:
                score += 1
            if board[i] == opp:
                score += -1
        return score*moves*10

def potmob(board, token, opp):
    mpot = 0
    opot = 0
    for i in range(11, 89):
        if board[i] == ".":
            if nextToOpp(board, token, i):
                mpot += 1
            if nextToOpp(board, opp, i):
                opot += 1
    return mpot, opot
