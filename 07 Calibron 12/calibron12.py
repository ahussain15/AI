# Aaliya Hussain
# 2nd Period
# 11/25/19

import sys

puzzle = sys.argv[1].split()
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

def goal_test(str):
    return "." not in str

def get_next_var(str):
    for i in range(len(str)):
        if str[i] == ".":
            if i == 0 or (i < puzzle_width or (str[i-puzzle_width] == "x")) and (i % puzzle_width == 0 or str[i-1] == "x"):
                tl = i
                w = 1
                for k in range(1, puzzle_width-(i%puzzle_width)):
                    if str[i+k] == "x":
                        break
                    w += 1
                return tl, w
    return None

def get_sorted_vals(ab, var):
    poss = []
    for r in ab:
        rw = max(r[0], r[1])
        rh = min(r[0], r[1])
        if var[1] >= rw and puzzle_height - int(var[0]/puzzle_width) >= rh:
            poss.append((r, rw, rh, var[0]%puzzle_width, int(var[0]/puzzle_width)))
        if rh != rw and var[1] >= rh and puzzle_height - int(var[0]/puzzle_width) >= rw:
            poss.append((r, rh, rw, var[0] % puzzle_width, int(var[0] / puzzle_width)))
    return poss

def coor_to_index(x, y):
    if y == 0:
        return x
    return int(x+puzzle_width*y)

def assign(str, ab, val, pll):
    nstr = str
    for x in range(0, val[1]):
        for y in range(0, val[2]):
            ci = coor_to_index(x+val[3], y+val[4])
            sl = list(nstr)
            sl[ci] = "x"
            nstr = "".join(sl)
    npll = pll.copy()
    npll.append((val[1], val[2], val[3], val[4]))
    nab = ab.copy()
    nab.remove(val[0])
    return nstr, nab, npll

def bt(str, ab, pll):
    if goal_test(str):
        return pll
    var = get_next_var(str)
    for val in get_sorted_vals(ab, var):
        a = assign(str, ab, val, pll)
        result = bt(a[0], a[1], a[2])
        if result is not None:
            return result
    return None

def check(l):
    s = "".join(["." for k in range(puzzle_height * puzzle_width)])
    for r in l:
        start = coor_to_index(r[2], r[3])
        if s[start] != ".":
            return False
        else:
            for x in range(0, r[0]):
                for y in range(0, r[1]):
                    ci = coor_to_index(r[2]+x, r[3]+y)
                    if s[ci] != ".":
                        return False
                    sl = list(s)
                    sl[ci] = "x"
                    s = "".join(sl)
    return "." not in s

if not check_sum(puzzle_height, puzzle_width, rectangles):
    print("Containing rectangle incorrectly sized.")
else:
    rect_list = sort_rects(rectangles)
    solution = bt("".join(["." for k in range(puzzle_width*puzzle_height)]), rect_list, list([]))
    if solution is None:
        print("No solution.")
    else:
        for r in solution:
            print("%s %s %s %s" % (r[3], r[2], r[1], r[0]))