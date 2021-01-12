# Aaliya Hussain
# 2nd Period
# 11/21/19

import sys

puzzle = "4 7 4x7".split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]

def check_sum(h, w, r):
    s = 0
    for sr in r:
        s += sr[0]*sr[1]
        if s > h*w:
            return False
    return s == h*w

def sort_rects(r):
    areas = []
    for i in range(len(r)):
        areas.append((r[i][0]*r[i][1], i))
    ret = [() for k in range(len(r))]
    areas = sorted(areas)[::-1]
    for j in range(len(r)):
        ret[j] = r[areas[j][1]]
    return ret

if not check_sum(puzzle_height, puzzle_width, rectangles):
    print("Containing rectangle incorrectly sized.")
else:
    rect_list = sort_rects(rectangles)

def coor_to_index(x, y):
    if y == 0:
        return x
    return int(x+puzzle_width*y)

def change(s, i):
    sl = list(s)
    sl[i] = "x"
    return "".join(sl)

def goal_test(l):
    if len(l) != len(rect_list):
        return False
    else:
        s = "".join(["." for k in range(puzzle_height*puzzle_width)])
        for r in l:
            start = coor_to_index(r[0], r[1])
            if s[start] != ".":
                return False
            else:
                for x in range(0, r[2]):
                    for y in range(0, r[3]):
                        ci = coor_to_index(r[0]+x, r[1]+y)
                        if s[ci] != ".":
                            return False
                        s = change(s, ci)
        return "." not in s

def get_next_var(l):
        return rect_list[len(l)]

def get_sorted_vals(l, var):
    poss = []
    rw = max(var[0], var[1])
    rh = min(var[0], var[1])
    for x in range(puzzle_width):
        for y in range(puzzle_height):
            addH = True
            if x+rw > puzzle_width or y+rh > puzzle_height:
                addH = False
            else:
                for ap in l:
                    if (x == ap[0] and y == ap[1]) or (((x > ap[0] and x < ap[0]+ap[2]) or (ap[0] > x and ap[0] < x+rw)) and ((ap[1] > y and ap[1]+ap[3] < y+rh) or (y > ap[1] and y+rh < ap[1]+ap[3]))):
                        addH = False
                        break
            if addH:
                poss.append((x, y, rw, rh))
            if rh != rw:
                addV = True
                if x+rh > puzzle_width or y+rw > puzzle_height:
                    addV = False
                else:
                    for ap in l:
                        if (x == ap[0] and y == ap[1]) or (((x > ap[0] and x < ap[0]+ap[2]) or (ap[0] >= x and ap[0] <= x+rh)) and ((y > ap[1] and y+rw < ap[1]+ap[3]) or (ap[1] > y and ap[1]+ap[3] < y+rw))):
                            addV = False
                            break
                if addV:
                    poss.append((x, y, rh, rw))
    return poss

def bt(l):
    if goal_test(l):
        return l
    elif len(l) >= len(rect_list):
        return None
    var = get_next_var(l)
    for val in get_sorted_vals(l, var):
        new_puzzle = l.copy()
        new_puzzle.append(val)
        result = bt(new_puzzle)
        if result is not None:
            return result
    return None

def check(l):
    s = "".join(["." for k in range(puzzle_height * puzzle_width)])
    for r in l:
        start = coor_to_index(r[0], r[1])
        if s[start] != ".":
            return False
        else:
            for x in range(0, r[2]):
                for y in range(0, r[3]):
                    ci = coor_to_index(r[0]+x, r[1]+y)
                    if s[ci] != ".":
                        return False
                    s = change(s, ci)
    return "." not in s

solution = bt(list([]))
if solution is None:
    print("No solution.")
else:
    print(check(solution))
    for r in solution:
        print("%s %s %s %s" % (r[1], r[0], r[3], r[2]))