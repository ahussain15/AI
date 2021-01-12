# Aaliya Hussain
# 2nd Period
# 10/25/19

import time
import random

def ir(state):
    while not goal_test(state):
        row = get_next_row(state)
        state[row] = get_next_value(state, row)
        #print("Conflicts: %s" % bc(state))
    return state

def get_next_row(state):
    max = 0
    for row in range(len(state)):
        if qc(state, row) > qc(state, max):
            max = row
        if qc(state, row) == qc(state, max):
            if random.randint(0, 3) != 0:
                max = row
    return max

def get_next_value(state, row):
    min = 0
    for c in range(len(state)):
        t = state.copy()
        tm = state.copy()
        t[row] = c
        tm[row] = min
        if bc(t) < bc(tm):
            min = c
        if bc(t) == bc(tm):
            if random.randint(0, 3) == 0:
                min = c
    return min


def qc(state, row):
    c = 0
    for r in range(len(state)):
        if state[r] == state[row] or abs((row-r)/(state[r]-state[row])) == 1:
            c += 1
    return c

def bc(state):
    c = 0
    # Columns
    cd = {co:state.count(co) for co in state}
    for co in cd:
        if cd[co] > 1:
            c += cd[co]-1
    # Diagonals
    ld = []
    for do in range(len(state)):
        ld.append(do + len(state) - 1 - state[do])
    dd = {do: ld.count(do) for do in ld}
    for do in dd:
        if dd[do] > 1:
            c += dd[do] - 1
    rd = []
    for do in range(len(state)):
        rd.append(do + state[do])
    dd = {do: rd.count(do) for do in rd}
    for do in dd:
        if dd[do] > 1:
            c += dd[do] - 1
    return c

def goal_test(state):
    return bc(state) == 0

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

bs = 45
print("Board size: %s" % bs)
ob = [random.randint(0, 100) for r in range(bs)]
print("Original board: %s" % ob)
print("Number of conflicts: %s " % bc(ob))
start = time.perf_counter()
sb = ir(ob)
end = time.perf_counter()
print("Solution: %s " % sb)
print("Time used: %s " % (end-start))
print("Solution test: %s " % test_solution(sb))