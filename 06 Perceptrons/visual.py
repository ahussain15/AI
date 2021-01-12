# Aaliya Hussain
# 2nd Period
# 5/30/20

import itertools
from matplotlib import pyplot

def truth_table(bits, n):
    table = [[tuple(vs)] for vs in itertools.product([1, 0], repeat=bits)]
    bin_rep = bin(n)[2:]
    for i in range(len(table)-len(bin_rep), len(table)):
        table[i].append(int(bin_rep[i-len(table)]))
    for i in range(0, len(table)-len(bin_rep)):
        table[i].append(0)
    return table

def step(num):
    if num > 0:
        return 1
    return 0

def perceptron(A, w, b, x):
    dot_p = 0
    for e in range(len(w)):
        dot_p += w[e]*x[e]
    return A(dot_p+b)

def check(tt, w, b):
    right = 0
    for i in range(len(tt)):
        p = perceptron(step, w, b, tt[i][0])
        if p == tt[i][1]:
            right += 1
    return right/len(tt)

def train(tt, bits):
    cur_w = [0 for i in range(bits)]
    cur_b = 0
    for e in range(100):
        stable = True
        for row in tt:
            f_star = perceptron(step, cur_w, cur_b, row[0])
            if f_star != row[1]:
                for i in range(bits):
                    cur_w[i] = cur_w[i]+(row[1]-f_star)*row[0][i]
                cur_b = cur_b+(row[1]-f_star)
                stable = False
        if stable:
            break
    return cur_w, cur_b

def eval_plot(f):
    tt = truth_table(2, f)
    vals = train(tt, 2)
    for v in range(len(tt)):
        if tt[v][1] == 1:
            pyplot.plot([tt[v][0][0]], [tt[v][0][1]], "go")
        else:
            pyplot.plot([tt[v][0][0]], [tt[v][0][1]], "ro")
    for x in range(-20, 21):
        for y in range(-20, 21):
            if (x/10 == 1 or x/10 == 0) and (y/10 == 1 or y/10 == 0):
                continue
            if perceptron(step, vals[0], vals[1], (x/10, y/10)) == 1:
                pyplot.plot([x/10], [y/10], "g.")
            else:
                pyplot.plot([x/10], [y/10], "r.")
    pyplot.show()

for f in range(16):
    eval_plot(f)
