# Aaliya Hussain
# 2nd Period
# 10/22/19

import time

def bt(state, meta):
    if goal_test(state):
        return state
    row = get_next_row(meta, state)
    for val in get_sorted_values(meta, row):
        ns = state.copy()
        ns[row] = val
        nm = update(meta, row, val)
        result = bt(ns, nm)
        if result is not None:
            return result
    return None

def goal_test(state):
    return -1 not in state

def get_next_row(meta, state):
    min = -1
    for r in range(len(meta)):
        if state[r] == -1 and min == -1:
            min = r
        if state[r] == -1 and len(meta[r]) < len(meta[min]):
            min = r
    return min

def get_sorted_values(meta, row):
    ret = []
    n = len(meta[row])
    if n > 0:
        if n % 2 == 1:
            c = n//2
            for k in range(n-c):
                ret.append(meta[row][c+k])
                ret.append(meta[row][c-k])
        else:
            c = n//2
            for k in range(n-c-1):
                ret.append(meta[row][c+k])
                ret.append(meta[row][c-k])
            ret.append(meta[row][0])
    return ret

def update(meta, row, c):
    ret = list(meta)
    for rm in range(len(ret)):
        if rm != row:
            t = list(ret[rm])
            for cm in meta[rm]:
                if cm in t and (cm == c or abs((rm-row)/(cm-c)) == 1):
                    t.remove(cm)
                    ret[rm] = tuple(t)
    return ret

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

# Board set up
bs = 211
meta = tuple([tuple([n for n in range(bs)]) for k in range(bs)])
board = [-1 for n in range(bs)]

for k in range(5):
# Solving
    start = time.perf_counter()
    sol = bt(board, meta)
    end = time.perf_counter()
# Output
    print("Size: %s" % bs)
    print(end-start)
    print(sol)
    print(test_solution(sol))
    print()