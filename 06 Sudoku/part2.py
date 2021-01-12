# Aaliya Hussain
# 2nd Period
# 12/6/19

from collections import deque
import sys
import time

n = 0
subblock_height = 0
subblock_width = 0
symbol_set = set()
letters = ["A", "B", "C", "D", "E", "F", "G"]
constraint = []
neighbors = []
cbi = dict()


def set_vars(l):
    global n
    global subblock_height
    global subblock_width
    global symbol_set
    global letters
    n = int(l ** 0.5)
    if n ** 0.5 == int(n ** 0.5):
        subblock_width = subblock_height = int(n ** 0.5)
    else:
        wt = max(int(n ** 0.5), int(round(n ** 0.5)))
        ht = n / wt
        while ht != int(ht):
            wt += 1
            ht = n / (wt)
        subblock_width = max(wt, int(ht))
        subblock_height = min(wt, int(ht))
    if n < 10:
        symbol_set = {str(k) for k in range(1, n + 1)}
    else:
        symbol_set = {str(k) for k in range(1, 10)}
        for s in range(n - 9):
            symbol_set.add(letters[s])


def constraints():
    global constraint
    sets = []
    # Rows
    for r in range(n):
        sets.append(set(k for k in range(r * n, (r + 1) * n)))
    # Columns
    for c in range(n):
        sets.append(set(k for k in range(c, n * n - (n - c) + 1, n)))
    # Blocks
    r = 0
    for b in range(n):
        t = set()
        for w in range(b * subblock_width + r * n, (b + 1) * subblock_width + r * n):
            for h in range(w, w + n * (subblock_height - 1) + 1, n):
                t.add(h)
        if (b + 1) % (n // subblock_width) == 0:
            r += subblock_height - 1
        sets.append(t)
    constraint = sets


def constrain():
    global neighbors
    global constraint
    nt = []
    for index in range(n * n):
        nt.append(set())
        for s in constraint:
            if index in s:
                for k in s:
                    if k != index:
                        nt[index].add(k)
    neighbors = nt


def goal_test(puzzle):
    return "." not in puzzle


def get_sorted_vals(puzzle, index):
    global neighbors
    ret = symbol_set.copy()
    for ni in neighbors[index]:
        if puzzle[ni] in ret:
            ret.remove(puzzle[ni])
    return ret


def possibilities(puzzle):
    fls = dict()
    for i in range(n * n):
        if puzzle[i] == ".":
            fls[i] = "".join(get_sorted_vals(puzzle, i))
        else:
            fls[i] = puzzle[i]
    return fls


def forward(puzzle, fl):
    pt = puzzle
    flt = fl.copy()
    ts = deque()
    for it in fl:
        if len(fl[it]) == 1:
            ts.append(it)
    while len(ts) != 0:
        it2 = ts.popleft()
        for ni in neighbors[it2]:
            t = set(flt[ni])
            if flt[it2] in t:
                if len(t) == 1:
                    return None
                t.remove(flt[it2])
                flt[ni] = "".join(t)
                if len(flt[ni]) == 1:
                    ts.append(ni)
        tp = list(pt)
        tp[it2] = flt[it2]
        pt = ''.join(tp)
    return pt, flt

def fc():
    global cbi
    for i in range(n*n):
        cbi[i] = []
        for c in range(len(constraint)):
            if i in constraint[c]:
                cbi[i].append(c)

def conprop(puzzle, fl):
    np = puzzle
    nfl = fl.copy()
    changed = []
    for con in range(len(constraint)):
        freq = dict()
        for i in constraint[con]:
            vals = list(nfl[i])
            for v in vals:
                if v not in freq:
                    freq[v] = list([i])
                else:
                    freq[v].append(i)
        if len(freq) != len(symbol_set):
            return None
        for v in freq.keys():
            if len(freq[v]) == 1:
                a = assign(np, nfl, freq[v][0], v)
                np = a[0]
                nfl = a[1]
                changed.append(freq[v][0])
    if len(changed) > 0:
        ft = forward(np, nfl)
        if ft is None:
            return None
        np = ft[0]
        nfl = ft[1]
    if np != puzzle:
        return np, nfl, True
    else:
        return np, nfl, False

def most_constrained(fl):
    min = -1
    for i in fl:
        if len(fl[i]) > 1:
            if min < 0:
                min = i
            if len(fl[i]) < len(fl[min]):
                min = i
    return min

def assign(puzzle, d, ci, cv):
    t = list(puzzle)
    t[ci] = cv
    ns = "".join(t)
    nd = d.copy()
    nd[ci] = str(cv)
    return ns, nd

def bt(puzzle, d):
    if goal_test(puzzle):
        return puzzle
    index = most_constrained(d)
    vals = list(d[index])
    for num in vals:
        a = assign(puzzle, d, index, num)
        ns = a[0]
        nd = a[1]
        ft = forward(ns, nd)
        if ft is not None:
            cpc = conprop(ft[0], ft[1])
            while cpc is not None and cpc[2]:
                ft = forward(cpc[0], cpc[1])
                cpc = conprop(ft[0], ft[1])
            if cpc is not None:
                result = bt(cpc[0], cpc[1])
                if result is not None:
                    return result
    return None

with open(sys.argv[1]) as f:
    for line in f:
        length = len(line.rstrip())
        set_vars(length)
        constraints()
        constrain()
        sfl = possibilities(line.rstrip())
        p = forward(line.rstrip(), sfl)
        if goal_test(p[0]):
            solution = p[0]
        else:
            fc()
            p2 = conprop(p[0], p[1])
            solution = bt(p2[0], p2[1])
        print(solution)


