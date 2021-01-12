# Aaliya Hussain
# 2nd Period

# Exercise 35
from nltk.corpus import words
import time

def coor_to_index(row, col, n):
    return int(col+n*row)

def index_to_coor(index, n):
    return int(index/n), int(index%n)

def pprint(board):
    n = int(len(board)**0.5)
    for x in range(n):
        print(board[x*n:n*x+n])

def all_n_words(n):
    all_words = words.words()
    n_words = list()
    for w in all_words:
        if len(w) == n and w not in n_words:
            n_words.append(w.lower())
    return n_words

def find_poss(d, blank):
    comp = "".join(["-" for k in range(len(blank))])
    if blank == comp:
        return d
    ret = []
    for w in d:
        isMatch = True
        for i in range(len(blank)):
            if blank[i] == "-" or blank[i] != w[i]:
                if blank[i] != "-":
                    isMatch = False
                break
        if isMatch:
            ret.append(w)
    return ret

def fill_blank(board, blank_num, word):
    b_list = list(board)
    for i in range(0, len(word)-blank_num):
        row_i = coor_to_index(blank_num+i, blank_num, len(word))
        col_i = coor_to_index(blank_num, blank_num+i, len(word))
        b_list[row_i] = word[i+blank_num]
        b_list[col_i] = word[i+blank_num]
    return "".join(b_list)

def backtrack(board, d):
    if "-" not in board:
        return board
    n = int(len(board)**0.5)
    num = index_to_coor(board.index("-"), n)[0]
    poss = find_poss(d, board[num*n:(num+1)*n])
    for w in poss:
        new_board = fill_blank(board, num, w)
        result = backtrack(new_board, d)
        if result is not None:
            return result
    return None

for k in range(8):
    n = k
    start_d = all_n_words(n)
    start_board = "".join(["-" for k in range(n*n)])
    start = time.perf_counter()
    answer = backtrack(start_board, start_d)
    end = time.perf_counter()
    pprint(answer)
    print(end-start)