# Aaliya Hussain
# 2nd Period
# 10/14/19

import sys
import time
from collections import deque

start = time.perf_counter()
groups = dict()
graph = dict()
with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        graph[line.rstrip()] = ()
        for x in range(0, 6):
            g = line.rstrip()[:x]+"*"+line.rstrip()[x+1:]
            if g not in groups:
                groups[g] = tuple([line.rstrip()])
            else:
                groups[g] += tuple([line.rstrip()])
                for w in groups[g]:
                    wset = set(graph[w])
                    bset = set(groups[g])
                    graph[w] = tuple(wset.union(bset))
        i += 1
end = time.perf_counter()
print("Time to create the data structure was: %s" % (end-start))
print("There are %s words in this dict." % i)
print()

def bfs(start, end):
    fringe = deque()
    visited = set()
    fringe.append((start, []))
    visited.add(start)
    while len(fringe) != 0:
        v = fringe.popleft()
        if v[0] == end:
            return v
        for n in graph[v[0]]:
            if n not in visited:
                t = v[1]+list([v[0]])
                fringe.append((n, t))
                visited.add(n)
    return None
def print_path(v):
    for s in v[1]:
        print(s)
    print(v[0])

start = time.perf_counter()
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
print("Time to solve all of these puzzles was %s seconds" % (start-end))