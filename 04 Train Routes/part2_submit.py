# Aaliya Hussain
# 2nd Period
# 10/21/19

from math import pi, acos, sin, cos
import heapq
from tkinter import *

# Sizing and placement
# (lat, long)
ul = (90, -180)
lr = (0, 0)
lc = 47
uc = 27
factor = 13

# Set up
window = Tk()
window.title("Train Routes Part 2")
canvas = Canvas(window, width=75*factor, height=50*factor)
canvas.pack()

# Helper methods
def dl(c1, c2, s):
    ll1 = graph[c1][:2]
    ll2 = graph[c2][:2]
    coor1 = ll_to_coors(ll1[0], ll1[1])
    coor2 = ll_to_coors(ll2[0], ll2[1])
    if s == "b":
        canvas.create_line(coor1[1], coor1[0], coor2[1], coor2[0])
    if s == "a":
        canvas.create_line(coor1[1], coor1[0], coor2[1], coor2[0], fill="red")
    if s == "d":
        canvas.create_line(coor1[1], coor1[0], coor2[1], coor2[0], fill="blue")
def ll_to_coors(lat, long):
    y_coor = (90-float(lat)-uc)*factor
    x_coor = (float(long)+180-lc)*factor
    return y_coor, x_coor
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

# Searching
def dijkstra(start, end):
    visited = set()
    fringe = [(0, start)]
    heapq.heapify(fringe)
    ac = 0
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
                    dl(v[1], n, "d")
                    ac += 1
                    if ac == 2500:
                        canvas.update()
                        canvas.update_idletasks()
                        window.update()
                        ac = 0
    return None
def astar(start, end):
    closed = set()
    fringe = [(0, start, 0)]
    heapq.heapify(fringe)
    ac = 0
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
                    dl(v[1], n, "a")
                    ac += 1
                    if ac == 600:
                        canvas.update()
                        canvas.update_idletasks()
                        window.update()
                        ac = 0
    return None

# Building data structures for searches
cities = dict()
with open("rrNodeCity.txt") as f:
    for line in f:
        data = line.rstrip().split()
        if len(data) == 2:
            cities[data[1]] = data[0]
        else:
            cities[' '.join(data[1:])] = data[0]
graph = dict()
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
        dl(data[0], data[1], "b")
        graph[data[0]] = graph[data[0]] + (data[1], gcd)
        graph[data[1]] = graph[data[1]] + (data[0], gcd)

# Graphics and searching
c1 = sys.argv[1]
c2 = sys.argv[2]
astar(cities[c1], cities[c2])
dijkstra(cities[c1], cities[c2])
window.mainloop()


