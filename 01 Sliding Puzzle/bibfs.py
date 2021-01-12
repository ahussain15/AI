# Aaliya Hussain
# 2nd Period
# 10/25/19

from collections import deque
import time
import sys

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
    fringe.append((state, []))
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.popleft()
        if v[0] == find_goal(state):
            return len(v[1])
        for c in get_children(v[0]):
            if c not in visited:
                t = v[1]+list([v[0]])
                fringe.append((c, t))
                visited.add(c)
    return None

def bibfs(state):
    ffringe = deque()
    bfringe = deque()
    fvisited = dict()
    bvisited = dict()
    ffringe.append((state, []))
    bfringe.append((find_goal(state), []))
    fvisited[state] = tuple([])
    bvisited[find_goal(state)] = tuple([])
    while len(ffringe) != 0 or len(bfringe) != 0:
        vf = ffringe.popleft()
        if vf[0] == find_goal(state):
            return len(vf[1])
        for c in get_children(vf[0]):
            if c in bvisited:
                return len(vf[1]+list([vf[0]])+list(bvisited[c]))
            if c not in fvisited:
                t = vf[1]+list([vf[0]])
                ffringe.append((c, t))
                fvisited[c] = tuple(t)
        vb = bfringe.popleft()
        if vb[0] == state:
            return len(vb[1])
        for c in get_children(vb[0]):
            if c in fvisited:
                return len(list(fvisited[c])+vb[1]+list([vb[0]]))
            if c not in bvisited:
                t = vb[1]+list([vb[0]])
                bfringe.append((c, t))
                bvisited[c] = tuple(t)
    return None

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        start = time.perf_counter()
        b1 = bfs(line[2:].rstrip())
        end = time.perf_counter()
        print("Line %s: %s, BFS - %s moves found in %s seconds" %(i, line[2:].rstrip(), b1, (end-start)))
        start = time.perf_counter()
        b2 = bibfs(line[2:].rstrip())
        end = time.perf_counter()
        print("Line %s: %s, BiBFS - %s moves found in %s seconds" % (i, line[2:].rstrip(), b2, (end - start)))
        i += 1