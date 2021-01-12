# Aaliya Hussain
# 9/23/19
# 2nd Period

from collections import deque
import sys
import time
import heapq

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

def parity(board):
    n = 0
    s = board.replace(".", "")
    order = ''.join(sorted(s))
    for c in s:
        for x in range(s.index(c), len(s)):
            if c > s[x]:
                n += 1
    if len(board) % 2 == 0:
        n += (len(board)**.5) - (index_to_coor(board.index("."), len(board)**.5)[0])
    return n

def txd(board):
    d = 0
    order = ''.join(sorted(board)[1:]+list(sorted(board)[0]))
    for c in board:
        if c != "." and board.index(c) != order.index(c):
            r1, c1 = index_to_coor(board.index(c), len(board)**.5)
            r2, c2 = index_to_coor(order.index(c), len(board)**.5)
            d += abs(r1-r2)+abs(c1-c2)
    return d

def bfs(state):
    fringe = deque()
    visited = set()
    fringe.append((state, 0))
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.popleft()
        if v[0] == find_goal(state):
            return v[1]
        else:
            for c in get_children(v[0]):
                if c not in visited:
                    fringe.append((c, v[1]+1))
                    visited.add(c)
    return None

def kdfs(state, k):
    fringe = deque()
    fringe.append((state, 0, {state}))
    while len(fringe) != 0:
        v = fringe.pop()
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
    b = kdfs(state, k)
    while b is None:
        k += 1
        b = kdfs(state, k)
    return b

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

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        args = line.rstrip().split(" ")
        print("Line %s: " % i, end='')
        print("", args[1], end='')
        start = time.perf_counter()
        n = parity(args[1])
        end = time.perf_counter()
        if (int(args[0]) % 2 != 0 and n % 2 != 0) or (int(args[0]) % 2 == 0 and n % 2 == 0):
            print(", no solution determined in %s seconds" % (end-start))
        else:
            if args[2] == "A":
                print(", A* - ", end='')
                start = time.perf_counter()
                m = astar(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end-start)))
            if args[2] == "B":
                print(", BFS - ", end='')
                start = time.perf_counter()
                m = bfs(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end - start)))
            if args[2] == "I":
                print(", ID-DFS - ", end='')
                start = time.perf_counter()
                m = iddfs(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end - start)))
            if args[2] == "!":
                print(", BFS - ", end='')
                start = time.perf_counter()
                m = bfs(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end - start)))
                print("Line %s: " % i, end='')
                print("", args[1], end='')
                print(", ID-DFS - ", end='')
                start = time.perf_counter()
                m = iddfs(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end - start)))
                print("Line %s: " % i, end='')
                print("", args[1], end='')
                print(", A* - ", end='')
                start = time.perf_counter()
                m = astar(args[1])
                end = time.perf_counter()
                print("%s moves in %s seconds" % (m, (end - start)))
        print()
        i += 1