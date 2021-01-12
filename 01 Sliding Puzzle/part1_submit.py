# Aaliya Hussain
# 2nd Period
# 9/13/19

import sys
from collections import deque
import time

def print_puzzle(size, rep):
    for x in range(size):
        print(" ".join(rep[size*x:size*(x+1)]))

def find_goal(board):
    return "".join(sorted(board)[1:])+"."

def coor_to_index(r, c, size):
    if r == 0:
        return int(c)
    return int(c+size*r)

def index_to_coor(i, size):
    if i < size:
        return 0, int(i)
    return int(i/size), int(i%size)

def swap(state, a, b):
    sl = list(state)
    sl[a], sl[b] = sl[b], sl[a]
    return ''.join(sl)

def get_children(state):
    size = int(len(state)**.5)
    r = index_to_coor(state.index("."), size)[0]
    c = index_to_coor(state.index("."), size)[1]
    cp = state.index(".")
    ret = []
    # Up
    if r > 0:
        np = coor_to_index(r-1, c, size)
        ret.append(swap(state, np, cp))
    # Down
    if r < size-1:
        np = coor_to_index(r+1, c, size)
        ret.append(swap(state, np, cp))
    # Left
    if c > 0:
        np = coor_to_index(r, c-1, size)
        ret.append(swap(state, np, cp))
    # Right
    if c < size-1:
        np = coor_to_index(r, c+1, size)
        ret.append(swap(state, np, cp))
    return ret

def goal_test(board):
    return board == find_goal(board)

def bfs(state):
    fringe = deque()
    visited = set()
    fringe.append((state, 0))
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.popleft()
        if goal_test(v[0]):
            return v[1]
        else:
            for c in get_children(v[0]):
                if c not in visited:
                    fringe.append((c, v[1]+1))
                    visited.add(c)
    return None

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        print("Line %s: " % i, end='')
        print("", line[2:].rstrip(), end='')
        start = time.perf_counter()
        print(", ", bfs(line[2:].rstrip()), end='')
        end = time.perf_counter()
        print(" moves found in %s seconds" % (end-start))
        i += 1