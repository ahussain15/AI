# Aaliya Hussain
# 2nd Period
# 2/13/20

import sys
import re
import math

def print_board(board, rows, cols):
    for k in range(rows):
        print(" ".join(board[k*cols:(k+1)*cols]))
    print()

def coor_to_index(row, col, cols):
    return int(col+cols*row)

def index_to_coor(index, cols):
    return int(index/cols), int(index%cols)

def place_words(word_list, board, rows, cols, num_blocks):
    alr_blocks = []
    mod_board = list(board)
    for w in range(len(word_list)):
        cur = re.split("(\d+)", word_list[w].lower())
        word = cur[4]
        for l in range(len(word)):
            if cur[0] == "h":
                next_i = coor_to_index(int(cur[1]), int(cur[3])+l, cols)
            else:
                next_i = coor_to_index(int(cur[1])+l, int(cur[3]), cols)
            if word[l] == "#":
                alr_blocks.append(next_i)
            mod_board[next_i] = word[l]
    #print_board("".join(mod_board), rows, cols)
    for bi in alr_blocks:
        mod_board[-(bi+1)] = "#"
    if len(alr_blocks) > 0:
        ret = implied("".join(mod_board), rows, cols, num_blocks)
        return ret
    return "".join(mod_board)

def fail(board, rows, cols):
    #print_board(board, rows, cols)
    for r in range(math.ceil(rows/2)):
        for l in range(cols):
            i = coor_to_index(r, l, cols)
            # Beginning: too short if --#, -#,
            if l == 0:
                if board[i] != "#" and (board[i+1] == "#" or (board[i+1] != "#" and board[i+2] == "#")):
                    return True
            # End case 1: too short if #--
            if l == cols-3:
                if board[i] == "#" and board[i+1] != "#" and board[i+2] != "#":
                    return True
            # End case 2: too short if #-
            if l == cols-2:
                if board[i] == "#" and board[i+1] != "#":
                    return True
                # Middle cases
            if l < cols-1:
                # Case 1: #-#
                if board[i] != "#" and board[i-1] == "#" and board[i+1] == "#":
                    return True
                # Case 2: #--#
            if l < cols-2:
                if board[i] != "#" and board[i+1] != "#" and board[i-1] == "#" and board[i+2] == "#":
                    return True
    # Cols
    for c in range(math.ceil(cols/2)):
        for l in range(rows):
            i = coor_to_index(l, c, cols)
            # Beginning: too short if --#, -#, --[letter]. -[letter]
            if l == 0:
                if board[i] != "#" and (board[i + cols] == "#" or (board[i + cols] != "#" and board[i + 2*cols] == "#")):
                    return True
                # End case 1: too short if #--, [letter]--
            if l == rows - 3:
                if board[i] == "#" and board[i + cols] != "#" and board[i + 2*cols] != "#":
                    return True
                # End case 2: too short if #-, [letter]-
            if l == rows - 2:
                if board[i] == "#" and board[i + cols] != "#":
                    return True
                # Middle cases
            if l < rows-1:
                # Case 1: #-#
                if board[i] != "#" and board[i - cols] == "#" and board[i + cols] == "#":
                    return True
                    # Case 2: #--#
            if l < rows-2:
                if board[i] != "#" and board[i + cols] != "#" and board[i - cols] == "#" and board[i + 2*cols] == "#":
                    return True
    if "-" not in board:
        return False
    start = board.index("-")
    r_start = index_to_coor(start, cols)[0]
    c_start = index_to_coor(start, cols)[1]
    q = []
    mod_board = list(board)
    mod_board[start] = "*"
    # Neighbors of start
    if r_start != 0 and mod_board[coor_to_index(r_start - 1, c_start, cols)] != "#":
        q.append(coor_to_index(r_start - 1, c_start, cols))
    if r_start != rows - 1 and mod_board[coor_to_index(r_start + 1, c_start, cols)] != "#":
        q.append(coor_to_index(r_start + 1, c_start, cols))
    if c_start != 0 and mod_board[coor_to_index(r_start, c_start - 1, cols)] != "#":
        q.append(coor_to_index(r_start, c_start - 1, cols))
    if c_start != cols - 1 and mod_board[coor_to_index(r_start, c_start + 1, cols)] != "#":
        q.append(coor_to_index(r_start, c_start + 1, cols))
    while q:
        cur = q.pop()
        mod_board[cur] = "*"
        cur_r = index_to_coor(cur, cols)[0]
        cur_c = index_to_coor(cur, cols)[1]
        if cur_r != 0 and mod_board[coor_to_index(cur_r - 1, cur_c, cols)] != "#" and mod_board[
            coor_to_index(cur_r - 1, cur_c, cols)] != "*":
            q.append(coor_to_index(cur_r - 1, cur_c, cols))
        if cur_r != rows - 1 and mod_board[coor_to_index(cur_r + 1, cur_c, cols)] != "#" and mod_board[
            coor_to_index(cur_r + 1, cur_c, cols)] != "*":
            q.append(coor_to_index(cur_r + 1, cur_c, cols))
        if cur_c != 0 and mod_board[coor_to_index(cur_r, cur_c - 1, cols)] != "#" and mod_board[
            coor_to_index(cur_r, cur_c - 1, cols)] != "*":
            q.append(coor_to_index(cur_r, cur_c - 1, cols))
        if cur_c != cols - 1 and mod_board[coor_to_index(cur_r, cur_c + 1, cols)] != "#" and mod_board[
            coor_to_index(cur_r, cur_c + 1, cols)] != "*":
            q.append(coor_to_index(cur_r, cur_c + 1, cols))
    for i in range(len(mod_board)):
        if mod_board[i] == "-":
            return True
    return False

def backtrack(board, rows, cols, num_blocks):
    if board is None:
        return None
    placed = board.count("#")
    if placed == num_blocks:
        if not fail(board, rows, cols):
            return board
        else:
            return None
    if placed > num_blocks:
        return None
    for i in range(board.index("-"), math.ceil(len(board)/2)):
        if board[i] == "-" and board[-(i+1)] == "-":
            next = i
            mod_board = list(board)
            mod_board[next] = "#"
            mod_board[-(next+1)] = "#"
            new_board = implied("".join(mod_board), rows, cols, num_blocks)
            if new_board is not None:
                result = backtrack(new_board, rows, cols, num_blocks)
                if result is not None:
                    return result
    return None

def implied(board, rows, cols, num_blocks): #returns None as soon failure is detected
    too_short = find_short(board, rows, cols)
    if too_short is None:
        return None
    tspi = too_short.count("#")
    if tspi > num_blocks:
        return None
    if tspi == num_blocks:
        return too_short
    uncon = area_fill(too_short, rows, cols)
    mod_board = list(too_short)
    for i in uncon:
        if mod_board[i] != "-" and mod_board[i] != "#":
            return None
        mod_board[i] = "#"
    return "".join(mod_board)

def find_short(board, rows, cols):
    change = set()
    cur_check = board
    go = True
    # Rows
    while cur_check is not None and go:
        #print_board(cur_check, rows, cols)
        for r in range(math.ceil(rows/2)):
            for l in range(cols):
                i = coor_to_index(r, l, cols)
            # Beginning: too short if --#, -#,
                if l == 0:
                    if cur_check[i] != "#" and cur_check[i+1] == "#":
                        change.add(i)
                    if cur_check[i] != "#" and cur_check[i+1] != "#" and cur_check[i+2] == "#":
                        change.add(i)
                        change.add(i+1)
            # End case 1: too short if #--
                if l == cols-3:
                    if cur_check[i] == "#" and cur_check[i+1] != "#" and cur_check[i+2] != "#":
                        change.add(i+1)
                        change.add(i+2)
            # End case 2: too short if #-
                if l == cols-2:
                    if cur_check[i] == "#" and cur_check[i+1] != "#":
                        change.add(i+1)
                # Middle cases
                if l < cols-1:
                # Case 1: #-#
                    if cur_check[i] != "#" and cur_check[i-1] == "#" and cur_check[i+1] == "#":
                        change.add(i)
                # Case 2: #--#
                if l < cols-2:
                    if cur_check[i] != "#" and cur_check[i+1] != "#" and cur_check[i-1] == "#" and cur_check[i+2] == "#":
                        change.add(i)
                        change.add(i+1)
    # Cols
        for c in range(math.ceil(cols/2)):
            for l in range(rows):
                i = coor_to_index(l, c, cols)
            # Beginning: too short if --#, -#, --[letter]. -[letter]
                if l == 0:
                    if cur_check[i] != "#" and cur_check[i + cols] == "#":
                        change.add(i)
                    if cur_check[i] != "#" and cur_check[i + cols] != "#" and cur_check[i + 2*cols] == "#":
                        change.add(i)
                        change.add(i + cols)
                # End case 1: too short if #--, [letter]--
                if l == rows - 3:
                    if cur_check[i] == "#" and cur_check[i + cols] != "#" and cur_check[i + 2*cols] != "#":
                        change.add(i + cols)
                        change.add(i + 2*cols)
                # End case 2: too short if #-, [letter]-
                if l == rows - 2:
                    if cur_check[i] == "#" and cur_check[i + cols] != "#":
                        change.add(i + cols)
                # Middle cases
                if l < rows-1:
                # Case 1: #-#, [letter]-[letter]
                    if cur_check[i] != "#" and cur_check[i - cols] == "#" and cur_check[i + cols] == "#":
                        change.add(i)
                    # Case 2: #--#, [letter]--[letter]
                if l < rows-2:
                    if cur_check[i] != "#" and cur_check[i + cols] != "#" and cur_check[i - cols] == "#" and cur_check[i + 2*cols] == "#":
                        change.add(i)
                        change.add(i + cols)
        if len(change) > 0:
            cur_check = update(cur_check, change)
            change = set()
        else:
            go = False
    return cur_check

def update(board, change):
    mod_board = list(board)
    for ch_i in change:
        if (mod_board[ch_i] != "-" and mod_board[ch_i] != "#") or (mod_board[-(ch_i+1)] != "-" and mod_board[-(ch_i+1)] != "#"):
            return None
        mod_board[ch_i] = "#"
        mod_board[-(ch_i + 1)] = "#"
    return "".join(mod_board)

def area_fill(board, rows, cols):
    start = board.index("-")
    r_start = index_to_coor(start, cols)[0]
    c_start = index_to_coor(start, cols)[1]
    q = []
    mod_board = list(board)
    mod_board[start] = "*"
    # Neighbors of start
    if r_start != 0 and mod_board[coor_to_index(r_start-1, c_start, cols)] != "#":
        q.append(coor_to_index(r_start-1, c_start, cols))
    if r_start != rows-1 and mod_board[coor_to_index(r_start+1, c_start, cols)] != "#":
        q.append(coor_to_index(r_start + 1, c_start, cols))
    if c_start != 0 and mod_board[coor_to_index(r_start, c_start-1, cols)] != "#":
        q.append(coor_to_index(r_start, c_start-1, cols))
    if c_start != cols-1 and mod_board[coor_to_index(r_start, c_start+1, cols)] != "#":
        q.append(coor_to_index(r_start, c_start+1, cols))
    while q:
        cur = q.pop()
        mod_board[cur] = "*"
        cur_r = index_to_coor(cur, cols)[0]
        cur_c = index_to_coor(cur, cols)[1]
        if cur_r != 0 and mod_board[coor_to_index(cur_r - 1, cur_c, cols)] != "#" and mod_board[coor_to_index(cur_r - 1, cur_c, cols)] != "*":
            q.append(coor_to_index(cur_r - 1, cur_c, cols))
        if cur_r != rows - 1 and mod_board[coor_to_index(cur_r + 1, cur_c, cols)] != "#" and mod_board[coor_to_index(cur_r + 1, cur_c, cols)] != "*":
            q.append(coor_to_index(cur_r + 1, cur_c, cols))
        if cur_c != 0 and mod_board[coor_to_index(cur_r, cur_c-1, cols)] != "#" and mod_board[coor_to_index(cur_r, cur_c-1, cols)] != "*":
            q.append(coor_to_index(cur_r, cur_c-1, cols))
        if cur_c != cols - 1 and mod_board[coor_to_index(cur_r, cur_c+1, cols)] != "#" and mod_board[coor_to_index(cur_r, cur_c+1, cols)] != "*":
            q.append(coor_to_index(cur_r, cur_c+1, cols))
    ret = set()
    #print_board("".join(mod_board), rows, cols)
    for i in range(len(mod_board)):
        if mod_board[i] == "-":
            ret.add(i)
            ret.add(rows*cols-(i+1))
    return list(ret)

def place_center(board):
    mod_board = list(board)
    mod_board[int(len(board)/2)] = "#"
    return "".join(mod_board)


# rows = 9
# cols = 13
# blocks = 32
# words = ["V5x0#", "V8x3#", "H3x9#", "V0x6Inclement"]

rows = int(sys.argv[1].split("x")[0])
cols = int(sys.argv[1].split("x")[1])
blocks = int(sys.argv[2])
words = sys.argv[4:]

board = "".join("-" for k in range(rows*cols))
wboard = place_words(words, board, rows, cols, blocks)
if rows*cols % 2 != 0 and blocks % 2 != 0:
    cboard = place_center(wboard)
    fboard = backtrack(cboard, rows, cols, blocks)
else:
    fboard = backtrack(wboard, rows, cols, blocks)
if fboard is not None:
    print_board(fboard, rows, cols)
