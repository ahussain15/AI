# Aaliya Hussain
# 2nd Period
# 10/7/19

# All data gathering code commented out to avoid crashing Mr. Eckel's computer.

import heapq
import time
import random
from collections import deque

# Sliding puzzle code necessary for multiple extensions
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

# A* and taxicab distance as implemented in part 2
def astar(state):
    closed = set()
    fringe = [(txd(state), state, 0)]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        if v[1] == find_goal(state):
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            for c in get_children(v[1]):
                heapq.heappush(fringe, (txd(c)+v[2]+1, c, v[2]+1))
    return None

def txd(board):
    d = 0
    order = ''.join(sorted(board)[1:]+list(sorted(board)[0]))
    for c in board:
        if c != "." and board.index(c) != order.index(c):
            r1, c1 = index_to_coor(board.index(c), len(board)**.5)
            r2, c2 = index_to_coor(order.index(c), len(board)**.5)
            d += abs(r1-r2)+abs(c1-c2)
    return d

# Code for extension A
def m_astar(state, m):
    closed = set()
    fringe = [(txd(state), state, 0)]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        if v[1] == find_goal(state):
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            for c in get_children(v[1]):
                heapq.heappush(fringe, (txd(c) + m*(v[2] + 1), c, v[2] + 1))
    return None

# Data gathering
# with open("15_puzzles.txt") as f:
#     i = 0
#     for line in f:
#         if i < 41:
#             state = line.rstrip()
#             print("Puzzle: %s" % state)
#             for m in range(10, 0, -1):
#                 start = time.perf_counter()
#                 s = m_astar(state, m/10)
#                 end = time.perf_counter()
#                 print("%s moves in %s seconds" % (s, end-start))
#                 print()
#         i += 10       #no particular reason for choosing to increment by 10 (10 is just a nice round number)

# Code for extension B
def rm_astar(state):
    closed = set()
    fringe = [(txd(state), random.random(), state, [])]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        if v[2] == find_goal(state):
            return v[3]
        if v[2] not in closed:
            closed.add(v[2])
            for c in get_children(v[2]):
                t = v[3] + list([c])
                heapq.heappush(fringe, (txd(c) + 0.4 * (len(v[3]) + 1), random.random(), c, t)) #m = 0.4, 0.5, 0.6
    return None

#Data gathering
# state = "JMGBILDFK.EONHCA" #55-move puzzle from 15_puzzles.txt
# for x in range(0, 15):
#     start = time.perf_counter()
#     s = rm_astar(state)
#     s2 = m_astar(state, 0.4) #m = 0.6, 0.5, 0.4
#     end = time.perf_counter()
#     print("%s moves in %s seconds" % (len(s), end-start))
#     print("%s moves in %s seconds" % (s2, end - start))
#     print()


# Code for extension D
nodes = 0
def bfs_np(state):
    global nodes
    fringe = deque()
    visited = set()
    fringe.append((state, 0))
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.popleft()
        nodes += 1
        if v[0] == find_goal(v[0]):
            return v[1]
        else:
            for c in get_children(v[0]):
                if c not in visited:
                    fringe.append((c, v[1] + 1))
                    visited.add(c)
    return None

def kdfs_np(state, k):
    global nodes
    fringe = deque()
    fringe.append((state, 0, {state}))
    while len(fringe) != 0:
        v = fringe.pop()
        nodes += 1
        if v[0] == find_goal(state):
            return v[1]
        if v[1] < k:
            for c in get_children(v[0]):
                if c not in v[2]:
                    t = v[2].union({c})
                    fringe.append((c, v[1]+1, t))
    return None
def iddfs(state):
    k = 0
    b = kdfs_np(state, k)
    while b is None:
        k += 1
        b = kdfs_np(state, k)
    return b

def astar_np(state):
    global nodes
    closed = set()
    fringe = [(txd(state), state, 0)]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        nodes += 1
        if v[1] == find_goal(state):
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            for c in get_children(v[1]):
                heapq.heappush(fringe, (txd(c) + v[2] + 1, c, v[2] + 1))
    return None

#Data gathering
# with open("15_puzzles.txt") as f:
#     for line in f:
#         state = line.rstrip()
#         start = time.perf_counter()
#         #moves = bfs_np(state)
#         #moves = iddfs(state)
#         moves = astar_np(state)
#         end = time.perf_counter()
#         if end-start > 10:
#             print("%s: %s moves" % (state, moves))
#             print("%s nodes per second" % (nodes/(end-start)))
#             break
#         nodes = 0

# Code for Extension C
rows = []
cols = []
def row_col(board):
    size = int(len(board)**0.5)
    letters = find_goal(board)
    for k in range(size):
        rows.append(set(letters[size*k:size*(k+1)]))
        cols.append(set(letters[k:size*size*size-(size-k)+1:size]))

def lin_con(board):
    size = int(len(board)**0.5)
    cons = 0
    for k in range(size):
        r = board[size*k:size*(k+1)]
        c = board[k:size * size * size - (size - k) + 1:size]
        for i in range(size-1):
            for j in range(i+1, size-1):
                if r[i] != "." and r[j] != ".":
                    if r[i] in rows[k] and r[j] in rows[k]:
                        if r[i] > r[j]:
                            cons += 2
                if c[i] != "." and c[j] != ".":
                    if c[i] in cols[k] and c[j] in cols[k]:
                        if c[i] > c[j]:
                            cons += 2
    return cons
