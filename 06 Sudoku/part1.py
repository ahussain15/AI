# Aaliya Hussain
# 2nd Period
# 11/1/19

import sys

n = 0
subblock_height = 0
subblock_width = 0
symbol_set = set()
letters = ["A", "B", "C", "D", "E", "F", "G"]
constraint = []
neighbors = []
recur = 0

def set_vars(l):
    global n
    global subblock_height
    global subblock_width
    global symbol_set
    global letters
    n = int(l ** 0.5)
    if n**0.5 == int(n**0.5):
        subblock_width = subblock_height = int(n**0.5)
    else:
        wt = max(int(n**0.5), int(round(n**0.5)))
        ht = n/wt
        while ht != int(ht):
            wt += 1
            ht = n/(wt)
        subblock_width = max(wt, int(ht))
        subblock_height = min(wt, int(ht))
    if n < 10:
        symbol_set = {str(k) for k in range(1, n+1)}
    else:
        symbol_set = {str(k) for k in range(1, 10)}
        for s in range(n-9):
            symbol_set.add(letters[s])

def print_puzzle(puzzle):
    global n
    for r in range(n):
        t = 0
        for c in range(n):
            if c != n-1:
                print(puzzle[n*r+c], end=" ")
            else:
                print(puzzle[n*r+c])
            if c%(n-1) != 0 and c % subblock_width == subblock_width-1:
                t += 1
                print("|", end=" ")
        if r%(n-1) != 0 and r%subblock_height == subblock_height-1:
            print(" ".join("-" for k in range(subblock_width*subblock_height+t)))
    print()

def constraints(puzzle):
    global constraint
    sets = []
    # Rows
    for r in range(n):
        sets.append(set(k for k in range(r*n, (r+1)*n)))
    # Columns
    for c in range(n):
        sets.append(set(k for k in range(c, n*n-(n-c)+1, n)))
    # Blocks
    r = 0
    for b in range(n):
        t = set()
        for w in range(b * subblock_width + r * n, (b + 1) * subblock_width + r * n):
            for h in range(w, w + n * (subblock_height - 1) + 1, n):
                t.add(h)
        if (b + 1) % (n // subblock_width) == 0:
            r += subblock_height-1
        sets.append(t)
    constraint = sets

def constrain(puzzle):
    global neighbors
    global constraint
    nt = []
    for index in range(n*n):
        nt.append(set())
        for s in constraint:
            if index in s:
                for k in s:
                    if k != index:
                        nt[index].add(k)
    neighbors = nt

def sym_count(puzzle):
    global symbol_set
    freq = {s:puzzle.count(str(s)) for s in symbol_set}
    for ch in freq:
        print("%s: %s" % (ch, freq[ch]))
    print()

def bt(puzzle):
    global recur
    recur += 1
    if goal_test(puzzle):
        return puzzle
    index = get_next_i(puzzle)
    vals = get_sorted_vals(puzzle, index)
    for num in vals:
        t = list(puzzle)
        t[index] = num
        ns = ''.join(t)
        result = bt(ns)
        if result is not None:
            return result
    return None

def goal_test(puzzle):
    return "." not in puzzle

def get_next_i(puzzle):
    return puzzle.index(".")

def get_sorted_vals(puzzle, index):
    global neighbors
    ret = symbol_set.copy()
    for ni in neighbors[index]:
        if puzzle[ni] in ret:
            ret.remove(puzzle[ni])
    return sorted(list(ret))

with open("sudoku_puzzles_1.txt") as f:
    for line in f:
        length = len(line.rstrip())
        set_vars(length)
        constraints(line.rstrip())
        constrain(line.rstrip())
        solution = bt(line.rstrip())
        print(recur)
        print(solution)
