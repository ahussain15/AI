# Aaliya Hussain
# 2nd Period
# 10/12/19

from math import pi, acos, sin, cos
import heapq
import sys
import time


def calcd(y1, x1, y2, x2):
    # y1 = lat1, x1 = long1
    # y2 = lat2, x2 = long2
    # all assumed to be in decimal degrees
    # if (and only if) the input is strings
    # use the following conversions
    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    R = 3958.76  # miles = 6371 km
    y1 *= pi / 180.0
    x1 *= pi / 180.0
    y2 *= pi / 180.0
    x2 *= pi / 180.0
    # approximate great circle distance with law of cosines
    return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * R

def dijkstra(start, end):
    visited = set()
    fringe = [(0, start)]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        if v[1] == end:
            return v[0]
        if v[1] not in visited:
            visited.add(v[1])
            neighbors = graph[v[1]][2:]
            for x in range(0, len(neighbors), 2):
                n = neighbors[x]
                if n != v[1]:
                    heapq.heappush(fringe, (neighbors[x+1]+v[0], n))
    return None

def astar(start, end):
    closed = set()
    fringe = [(0, start, 0)]
    heapq.heapify(fringe)
    while len(fringe) != 0:
        v = heapq.heappop(fringe)
        if v[1] == end:
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            neighbors = graph[v[1]][2:]
            for x in range(0, len(neighbors), 2):
                n = neighbors[x]
                if n != v[1]:
                    y1 = graph[end][0]
                    x1 = graph[end][1]
                    y2 = graph[n][0]
                    x2 = graph[n][1]
                    heapq.heappush(fringe, (neighbors[x+1]+v[2]+calcd(y1, x1, y2, x2), n, neighbors[x+1]+v[2]))
    return None

start = time.perf_counter()
# Auxiliary storage for city input
cities = dict()
with open("rrNodeCity.txt") as f:
    for line in f:
        data = line.rstrip().split()
        if len(data) == 2:
            cities[data[1]] = data[0]
        else:
            cities[' '.join(data[1:])] = data[0]
# Actual weighted graph
graph = dict()
# tag : tuple(lat, long, neighbor, gcd...)
with open("rrNodes.txt") as f:
    for line in f:
        data = line.rstrip().split()
        graph[data[0]] = tuple((data[1], data[2]))
with open("rrEdges.txt") as f:
    for line in f:
        data = line.rstrip().split()
        t1 = graph[data[0]]
        t2 = graph[data[1]]
        gcd = calcd(t1[0], t1[1], t2[0], t2[1])
        graph[data[0]] = graph[data[0]] + (data[1], gcd)
        graph[data[1]] = graph[data[1]] + (data[0], gcd)
end = time.perf_counter()
print("Time to create data structure: %s" % (end-start))

c1 = sys.argv[1]
c2 = sys.argv[2]
start = time.perf_counter()
d1 = dijkstra(cities[c1], cities[c2])
end = time.perf_counter()
print("%s to %s with Dijkstra: %s in %s seconds" % (c1, c2, d1, (end-start)))
start = time.perf_counter()
d2 = astar(cities[c1], cities[c2])
end = time.perf_counter()
print("%s to %s with A*: %s in %s seconds" % (c1, c2, d2, (end-start)))