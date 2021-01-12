# Aaliya Hussain
# 2nd Period
# 10/21/19

def bt(state, n):
    if goal_test(state, n):
        return state
    row = len(state)
    for val in get_sorted_values(state, row, n):
       ns = state+[val]
       result = bt(ns, n)
       if result is not None:
           return result
    return None

def goal_test(state, n):
    return len(state) == n

def get_sorted_values(state, var, n):
    ret = []
    for x in range(n):
        if x not in state and dc(state, var, x):
            ret.append(x)
    return ret

def dc(state, var, x):
    for k in range(var):
        if abs((var-k)/(x-state[k])) == 1:
            return False
    return True

print(bt([], 8))
print(bt([], 9))
print(bt([], 10))