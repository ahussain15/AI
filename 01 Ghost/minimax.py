# Aaliya Hussain
# 2nd Period
# 2/4/20

import sys

all_words = set()
valids = set()
next_let = dict()

def poss_words(d_file, min_len, prog):
    global longest
    with open(d_file) as f:
        for line in f:
            if len(line.rstrip()) >= min_len:
                if line.rstrip().isalpha():
                    if prog == "" or line.rstrip().lower()[:len(prog)] == prog.lower():
                        all_words.add(line.rstrip().lower())
                        find_next(line.rstrip().lower(), prog)
                        find_valid(line.rstrip().lower())

def find_valid(word):
    for e in range(len(word)+1):
        valids.add(word[:e].lower())

def find_next(word, prog):
    poss_next = word[len(prog):]
    for t in range(len(poss_next)):
        if t+len(prog) not in next_let:
            next_let[t+len(prog)] = list()
        if poss_next[t] not in next_let[t+len(prog)]:
            next_let[t+len(prog)].append(poss_next[t])

def is_over(current):
    return (current.lower() in all_words)

def is_valid(current):
    return (current.lower() in valids)

def min(current):
    if is_over(current):
        return -1
    n_moves = next_let[len(current)]
    cur_m = 2
    for l in n_moves:
        n_cur = current + l
        if is_valid(n_cur):
            m_poss = max(n_cur)
            if cur_m > m_poss:
                cur_m = m_poss
    return cur_m

def max(current):
    if is_over(current):
        return 1
    n_moves = next_let[len(current)]
    cur_m = -2
    for l in n_moves:
        n_cur = current + l
        if is_valid(n_cur):
            m_poss = min(n_cur)
            if cur_m < m_poss:
                cur_m = m_poss
    return cur_m

d_file = sys.argv[1]
min_len = int(sys.argv[2])
if len(sys.argv) > 3:
    prog = sys.argv[3].lower()
else:
    prog = ""

current = prog
poss_words(d_file, min_len, prog)
next = next_let[len(prog)]
wins = []
for n in next:
    n_cur = current+n
    if min(n_cur) > 0:
        wins.append(n)
if len(wins) > 0:
    print("Next player can win with any of these letters: %s" % wins)
else:
    print("Next player will lose!")