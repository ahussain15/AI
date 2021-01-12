# Aaliya Hussain
# Second Period
# 9/16/19

import sys
import time
from collections import deque

#Building the data structure (graph)
def is_next(w1, w2):
    d = 0
    for x in range(0, len(w1)):
        if w1[x] != w2[x]:
            d += 1
            if d > 1:
                return False
    return True
start = time.perf_counter()
graph = dict()
with open(sys.argv[1]) as f:
    for line in f:
        graph[line.rstrip()] = tuple([])
for w in graph:
    for pn in graph:
        if pn != w:
            if is_next(w, pn):
                t = list(graph[w]) + list([pn])
                graph[w] = tuple(t)
end = time.perf_counter()
print("Time to create the data structure was: %s" % (end-start))
print("There are %s words in this dict." % len(graph))
print()

#BFS
start = time.perf_counter()
def bfs(start, end):
    fringe = deque()
    visited = set()
    fringe.append((start, []))
    visited.add(start)
    while len(fringe) != 0:
        v = fringe.popleft()
        if v[0] == end:
            return v
        for c in graph[v[0]]:
            if c not in visited:
                t = v[1]+list([v[0]])
                fringe.append((c, t))
                visited.add(c)
    return None
def print_path(v):
    for s in v[1]:
        print(s)
    print(v[0])
with open(sys.argv[2]) as f:
    i = 0
    for line in f:
        print("Line: %s" % i)
        v = bfs(line[:6], line[7:13])
        if v is not None:
            print("Length is %s" % (len(v[1])+1))
            print_path(v)
        else:
            print("No solution!")
        print()
        i += 1
end = time.perf_counter()
print("Time to solve of all these puzzles was %s seconds" % (end-start))