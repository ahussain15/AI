# Aaliya Hussain
# 2nd Period
# 2/23/20

import sys

arith_cons = dict()
neighbors = dict()
size = 0

def coor_to_index(row, col):
    global size
    return int(col+size*row)

def index_to_coor(index):
    global size
    return int(index/size), int(index%size)

def setup(file):
    global size, arith_cons
    with open(file) as f:
        first = f.readline().rstrip()
        size = int(len(first)**0.5)
        board_0 = "".join("." for k in range(size**2))
        for li in range(len(first)):
            if first[li] not in arith_cons:
                arith_cons[first[li]] = [0, "", []]
            arith_cons[first[li]][2].append(li)
        for nac in range(len(arith_cons)):
            acs = f.readline().rstrip().split(" ")
            arith_cons[acs[0]][0] = int(acs[1])
            arith_cons[acs[0]][1] = acs[2]
    return board_0

def gen_neighbors():
    global neighbors, size
    for i in range(size**2):
        neighbors[i] = []
        row = index_to_coor(i)[0]
        col = index_to_coor(i)[1]
        # Row
        rstart = coor_to_index(row, 0)
        for ri in range(size):
            if i != (rstart+ri):
                neighbors[i].append(rstart+ri)
        # Col
        cstart = coor_to_index(0, col)
        for ci in range(size):
            if i != (cstart+ci*size):
                neighbors[i].append(cstart+ci*size)

def find_ac(index):
    for let in arith_cons:
        if index in arith_cons[let][2]:
            return let

def back_track(board):
    if "." not in board:
        return board
    i = board.index(".")
    let = find_ac(i)
    poss = get_poss(board, i, let)
    for p in poss:
        b_list = list(board)
        b_list[i] = p
        new_board = "".join(b_list)
        result = back_track(new_board)
        if result is not None:
            return result
    return None

def get_poss(board, i, let):
    tar_num = arith_cons[let][0]
    op = arith_cons[let][1]
    indices = arith_cons[let][2]
    poss = []
    if len(indices) < 3 and board[indices[0]] != ".":
        if op == "+":
            cor_val = [str(tar_num-int(board[indices[0]]))]
        elif op == "-":
            cor_val = [str(int(board[indices[0]])-tar_num)]
            cor_val.append(str(int(board[indices[0]])+tar_num))
        elif op == "*":
            cor_val = [str(tar_num/int(board[indices[0]]))]
        else:
            cor_val = [str(int(board[indices[0]])/tar_num)]
            cor_val.append(str(tar_num/int(board[indices[0]])))
            cor_val.append(str(tar_num*int(board[indices[0]])))
        for val in cor_val:
            if float(val).is_integer() and 1 <= float(val) <= size and str(int(float(val))) not in poss:
                poss.append(str(int(float(val))))
    else:
        poss = []
        if op == "+":
            for p in range(1, tar_num):
                if p > size:
                    break
                poss.append(str(p))
        if op == "-":
            for p in range(1, size+1):
                poss.append(str(p))
        if op == "x":
            for p in range(1, size+1):
                if tar_num % p == 0:
                    poss.append(str(p))
        if op == "/":
            for p in range(1, size+1):
                if p % tar_num == 0 or tar_num*p <= size:
                    poss.append(str(p))
        if len(indices) > 2 and board[indices[0]] != ".":
            if op == "+":
                cur = 0
            else:
                cur = 1
            for i2 in indices:
                if board[i2] != ".":
                    if op == "+":
                        cur += int(board[i2])
                    else:
                        cur *= int(board[i2])
            for p in poss:
                if op == "+":
                    if cur + int(p) > tar_num:
                        poss.remove(p)
                else:
                    if cur * int(p) > tar_num:
                        poss.remove(p)
    if poss:
        for ni in neighbors[i]:
            if board[ni] in poss:
                poss.remove(board[ni])
                if len(poss) == 0:
                    break
    return poss

start = setup(sys.argv[1])
gen_neighbors()
solution = back_track(start)
print(solution)

