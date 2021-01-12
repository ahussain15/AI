# Aaliya Hussain
# 2nd Period
# 3/1/20

import sys
import re
import math

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters_i = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

def coor_to_index(row, col, cols):
    return int(col+cols*row)

def index_to_coor(index, cols):
    return int(index/cols), int(index%cols)

def print_board(board):
    for k in range(rows):
        print(" ".join(board[k*cols:(k+1)*cols]))
    print()

def place_words(word_list, board, num_blocks):
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
        ret = implied("".join(mod_board), num_blocks)
        return ret
    return "".join(mod_board)

def fail(board):
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

def backtrack(board, num_blocks):
    if board is None:
        return None
    placed = board.count("#")
    if placed == num_blocks:
        if not fail(board):
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
            new_board = implied("".join(mod_board), num_blocks)
            if new_board is not None:
                result = backtrack(new_board, num_blocks)
                if result is not None:
                    return result
    return None

def implied(board, num_blocks): #returns None as soon failure is detected
    too_short = find_short(board)
    if too_short is None:
        return None
    tspi = too_short.count("#")
    if tspi > num_blocks:
        return None
    if tspi == num_blocks:
        return too_short
    uncon = area_fill(too_short)
    mod_board = list(too_short)
    for i in uncon:
        if mod_board[i] != "-" and mod_board[i] != "#":
            return None
        mod_board[i] = "#"
    return "".join(mod_board)

def find_short(board):
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

def area_fill(board):
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

def gen_dict(file):
    ret = dict()
    frags = dict()
    with open(file) as f:
        for line in f:
            line_s = line.rstrip().lower()
            if line_s.isalpha() and len(line_s) > 2:
                if len(line_s) not in ret:
                    # key = word_len; val = list[0 = freq count for each let; 1 = possible words of word_len]
                    ret[len(line_s)] = [[[letters[k], 0] for k in range(26)], set()]
                # Add to frags if shorter word
                if len(line_s) < 6:
                    frags = fragments(line_s, frags)
                # Add to possible word list
                ret[len(line_s)][1].add(line_s)
                # Update freq counts
                for l in line_s:
                    i_in_freq = letters_i[l]
                    ret[len(line_s)][0][i_in_freq][1] += 1
    return ret, frags

def fragments(word, frags):
    lets = [[word[k], "-"] for k in range(len(word))]
    if len(word) == 3:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    if lets[0][a] + lets[1][b] + lets[2][c] not in frags:
                        frags[lets[0][a] + lets[1][b] + lets[2][c]] = 0
                    frags[lets[0][a] + lets[1][b] + lets[2][c]] += 1
    if len(word) == 4:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        if lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d] not in frags:
                            frags[lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d]] = 0
                        frags[lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d]] += 1
    if len(word) == 5:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        for e in range(2):
                            if lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d]+lets[4][e] not in frags:
                                frags[lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d]+lets[4][e]] = 0
                            frags[lets[0][a] + lets[1][b] + lets[2][c] + lets[3][d]+lets[4][e]] += 1
    return frags

def rem_words(board):
    blank_list = []
    blank_to_index = dict()
    index_to_blank = dict()
    for r in range(rows):
        poss = re.finditer("#?[^#]+(?=-)[^#]+#?", board[cols*r:cols*(r+1)])
        for p in poss:
            if p.group()[0] == "#":
                start = coor_to_index(r, p.start()+1, cols)
            else:
                start = coor_to_index(r, p.start(), cols)
            if p.group()[-1] == "#":
                end = coor_to_index(r, p.end()-2, cols)
            else:
                end = coor_to_index(r, p.end() - 1, cols)
            blank_list.append((board[start:end+1], start, "h"))
            blank_to_index[len(blank_list)-1] = []
            for i in range(start, end+1):
                blank_to_index[len(blank_list)-1].append(i)
                if i not in index_to_blank:
                    index_to_blank[i] = []
                index_to_blank[i].append(len(blank_list)-1)
    for c in range(cols):
        poss = re.finditer("#?[^#]+(?=-)[^#]+#?", board[c:(rows*cols)-(cols-c-1):cols])
        for p in poss:
            if p.group()[0] == "#":
                start = coor_to_index(p.start() + 1, c, cols)
            else:
                start = coor_to_index(p.start(), c, cols)
            if p.group()[-1] == "#":
                end = coor_to_index(p.end()-2, c, cols)
            else:
                end = coor_to_index(p.end() - 1, c, cols)
            blank_list.append((board[start:end + 1:cols], start, "v"))
            blank_to_index[len(blank_list) - 1] = []
            for i in range(start, end + 1, cols):
                blank_to_index[len(blank_list) - 1].append(i)
                if i not in index_to_blank:
                    index_to_blank[i] = []
                index_to_blank[i].append(len(blank_list) - 1)
    return blank_list, blank_to_index, index_to_blank

def choose_next_blank(blank_list):
    min_freq_len = 3
    for blank in blank_list:
        if "-" in blank[0]:
            if len(blank[0]) > min_freq_len:
                min_freq_len = len(blank[0])
    cor_len_b = []
    if min_freq_len > 5:
        max_num_let = 0
        for bi in range(len(blank_list)):
            if len(blank_list[bi][0]) == min_freq_len and "-" in blank_list[bi][0]:
                cor_len_b.append(bi)
                num_let = min_freq_len - blank_list[bi][0].count("-")
                if num_let > max_num_let:
                    max_num_let = num_let
        cor_len_num = []
        for bi in cor_len_b:
            num_let = min_freq_len - blank_list[bi][0].count("-")
            if num_let == max_num_let:
                cor_len_num.append(bi)
        min_let_freq = 0
        most_con_i = cor_len_num[0]
        all_b = "".join(["-" for k in range(min_freq_len)])
        for bi in cor_len_num:
            if blank_list[bi][0] != all_b:
                let_freq = calc_avg_freq(blank_list[bi][0])
                if min_let_freq == 0 or let_freq < min_let_freq:
                    min_let_freq = let_freq
                    most_con_i = bi
    else:
        for bi in range(len(blank_list)):
            if len(blank_list[bi][0]) == min_freq_len and "-" in blank_list[bi][0]:
                cor_len_b.append(bi)
        most_con_i = cor_len_b[0]
        min_frag_freq = 0
        for bi in cor_len_b:
            if min_frag_freq == 0 or frags[blank_list[bi][0]] < min_frag_freq:
                min_frag_freq = frags[blank_list[bi][0]]
                most_con_i = bi
    return most_con_i

def calc_avg_freq(word):
    total_freq = 0
    for let in word:
        if let != "-":
            total_freq += word_info[len(word)][0][letters_i[let]][1]
    return int(total_freq/len(word))

def get_sorted_poss(board, word):
    ret_poss = []
    comp = "".join(["-" for k in range(len(word))])
    for poss in word_info[len(word)][1]:
        is_match = True
        if word != comp:
            for i in range(len(word)):
                if word[i] != "-":
                    if word[i] != poss[i]:
                        is_match = False
                        break
        if is_match and check_ap(board, poss):
            ret_poss.append((poss, calc_avg_freq(poss)))
    return reversed(sorted(ret_poss, key=lambda x:x[1]))

def check_ap(board, poss):
    for r in range(rows):
        if poss in board[r*cols:(r+1)*cols]:
            return False
    for c in range(cols):
        if poss in board[c:(rows*cols)-(cols-c-1):cols]:
            return False
    return True

def fill_blank(board, blank_list, blank_i, poss):
    nb_list = list(board)
    new_blanks = blank_list.copy()
    temp = list(new_blanks[blank_i])
    temp[0] = poss
    new_blanks[blank_i] = tuple(temp)
    changed_board = []
    for i_i in range(len(blank_to_index[blank_i])):
        if board[blank_to_index[blank_i][i_i]] != poss[i_i]:
            nb_list[blank_to_index[blank_i][i_i]] = poss[i_i]
            changed_board.append(blank_to_index[blank_i][i_i])
    new_board = "".join(nb_list)
    for cbi in changed_board:
        for cb in index_to_blank[cbi]:
            if cb != blank_i:
                i_to_ch = find_blank_i(cbi, blank_list[cb][1], blank_list[cb][2])
                temp = list(blank_list[cb])
                str_temp = list(temp[0])
                str_temp[i_to_ch] = nb_list[cbi]
                temp[0] = "".join(str_temp)
                if "-" not in temp[0]:
                    if temp[0] not in word_info[len(temp[0])][1]:
                        return None
                elif len(temp[0]) < 6:
                    if temp[0] not in frags:
                        return None
                new_blanks[cb] = tuple(temp)
    #print_board(new_board)
    return new_board, new_blanks

def find_blank_i(changed_i, start, dir):
    if dir == "h":
        return (changed_i-start)
    else:
        return int((changed_i-start)/cols)

def unique(blank_list):
    for w in range(len(blank_list)):
        for w2 in range(len(blank_list)):
            if w != w2 and blank_list[w][0] == blank_list[w2][0]:
                return False
    return True

def back_track_words(board, blank_list):
    if "-" not in board:
        if unique(blank_list):
            return board
        else:
            return None
    next_blank = choose_next_blank(blank_list)
    poss = get_sorted_poss(board, blank_list[next_blank][0])
    for p in poss:
        new = fill_blank(board, blank_list, next_blank, p[0])
        if new is not None:
            result = back_track_words(new[0], new[1])
            if result is not None:
                return result
    return None

rows = int(sys.argv[1].split("x")[0])
cols = int(sys.argv[1].split("x")[1])
blocks = int(sys.argv[2])
file = sys.argv[3]
words = sys.argv[4:]

# rows = 5
# cols = 5
# blocks = 0
# file = "twentyk.txt"
# words = ["V4x0S"]

sboard = "".join("-" for k in range(rows*cols))
wboard = place_words(words, sboard, blocks)
if rows*cols % 2 != 0 and blocks % 2 != 0:
    cboard = place_center(wboard)
    fboard = backtrack(cboard, blocks)
else:
    fboard = backtrack(wboard, blocks)

if fboard is not None:
    dicts = gen_dict(file)
    word_info = dicts[0]
    frags = dicts[1]
    look_ups = rem_words(fboard)
    blank_to_index = look_ups[1]
    index_to_blank = look_ups[2]
    dboard = back_track_words(fboard, look_ups[0])
    if dboard is not None:
        print_board(dboard)

