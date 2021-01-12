# Aaliya Hussain
# Second Period
# 9/30/19

from collections import deque

def coor_to_index(r, c):
    if r == 0:
        return int(c)
    return int(c+6*r)

def index_to_coor(i):
    if i < 6:
        return 0, int(i)
    return int(i/6), int(i%6)

def change(state, a, c):
    sl = list(state)
    sl[a] = c
    return ''.join(sl)

# b = (r, c, length/width, direction, goal_bool)
def make_board(blocks):
    rep = "...................................."
    for b in blocks:
        if b[4]:
            c = "g"
        else:
            if blocks.index(b) < 10:
                c = str(blocks.index(b))
            else:
                if blocks.index(b) == 10:
                    c = "A"
                if blocks.index(b) == 11:
                    c = "B"
                if blocks.index(b) == 12:
                    c = "C"
                if blocks.index(b) == 13:
                    c = "D"
                if blocks.index(b) == 14:
                    c = "E"
        start = coor_to_index(b[0], b[1])
        rep = change(rep, start, c)
        if b[3] == "v":
            for x in range(1, b[2]):
                o = coor_to_index(b[0]+x, b[1])
                rep = change(rep, o, c)
        if b[3] == "h":
            for x in range(1, b[2]):
                o = coor_to_index(b[0], b[1]+x)
                rep = change(rep, o, c)
    return rep

def print_board(rep):
    for x in range(6):
         print(" ".join(rep[6*x:6*(x+1)]))

def get_children(rep, oblocks):
    ret = []
    for b in oblocks:
        blocks = oblocks.copy()
        i = blocks.index(b)
        if b[3] == "v":
            #Up
            if b[0] > 0:
                for x in range(b[0]-1, -1, -1):
                    p = coor_to_index(x, b[1])
                    if rep[p] == ".":
                        blocks[i] = (x, b[1], b[2], b[3], b[4])
                        ret.append((make_board(blocks), blocks))
                        blocks = oblocks.copy()
                    else:
                        break
            #Down
            if (b[0]+b[2]-1) < 5:
                for x in range(b[0]+b[2], 6):
                    p = coor_to_index(x, b[1])
                    if rep[p] == ".":
                        blocks[i] = (x-(b[2]-1), b[1], b[2], b[3], b[4])
                        ret.append((make_board(blocks), blocks))
                        blocks = oblocks.copy()
                    else:
                        break
        if b[3] == "h":
            #Left
            if b[1] > 0:
                for x in range(b[1]-1, -1, -1):
                    p = coor_to_index(b[0], x)
                    if rep[p] == ".":
                        blocks[i] = (b[0], x, b[2], b[3], b[4])
                        ret.append((make_board(blocks), blocks))
                        blocks = oblocks.copy()
                    else:
                        break
            #Right
            if (b[1]+b[2]-1) < 5:
                for x in range(b[1]+b[2], 6):
                    p = coor_to_index(b[0], x)
                    if rep[p] == ".":
                        blocks[i] = (b[0], x-(b[2]-1), b[2], b[3], b[4])
                        ret.append((make_board(blocks), blocks))
                        blocks = oblocks.copy()
                    else:
                        break
    return ret

def goal_test(rep):
    return (rep[16] == "g" and rep[17] == "g")

def print_game(v):
    for s in v[2]:
        print_board(s)
        print()
    print_board(v[0])
    print()

def bfs(state, blocks):
    fringe = deque()
    visited = set()
    fringe.append((state, blocks, []))
    visited.add(state)
    while len(fringe) != 0:
        v = fringe.popleft()
        if goal_test(v[0]):
            print_game(v)
            return len(v[2])
        for c in get_children(v[0], v[1]):
            if c[0] not in visited:
                t = v[2]+list([v[0]])
                fringe.append((c[0], c[1], t))
                visited.add(c[0])
    return None

blocks = [(0, 0, 2, "v", False), (0, 3, 3, "h", False), (1, 2, 2, "h", False), (1, 4, 2, "h", False), (2, 0, 2, "h", True), (2, 2, 2, "v", False), (2, 5, 2, "v", False), (3, 0, 2, "h", False), (3, 3, 2, "v", False), (3, 4, 2, "v", False), (4, 0, 3, "h", False), (4, 5, 2, "v", False), (5, 0, 2, "h", False)]
rep = make_board(blocks)
#print_board(rep)
print(bfs(rep, blocks))
