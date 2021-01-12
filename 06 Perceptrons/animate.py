# Aaliya Hussain
# 2nd Period
# 6/8/20

import itertools, sys
from matplotlib import pyplot
import numpy

data_x = []
data_y = []

def find_pts():
    for x in range(-20, 21):
        for y in range(-20, 21):
            if (x/10 == 1 or x/10 == 0) and (y/10 == 1 or y/10 == 0):
                continue
            else:
                data_x.append(x/10)
                data_y.append(y/10)

find_pts()
x = numpy.array(data_x)
y = numpy.array(data_y)

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

def train(tt, bits, lambd):
    cur_w = [0 for i in range(bits)]
    cur_b = 0
    for e in range(100):
        stable = True
        animate(cur_w, cur_b)
        pyplot.show()
        for row in tt:
            f_star = perceptron(step, cur_w, cur_b, row[0])
            if f_star != row[1]:
                for i in range(bits):
                    cur_w[i] = cur_w[i]+(row[1]-f_star)*row[0][i]*lambd
                cur_b = cur_b+(row[1]-f_star)*lambd
                stable = False
        if stable:
            break

def animate(w, b):
    for v in range(len(tt)):
        if tt[v][1] == 1:
            pyplot.plot([tt[v][0][0]], [tt[v][0][1]], "go")
        else:
            pyplot.plot([tt[v][0][0]], [tt[v][0][1]], "ro")
    for k in range(len(x)):
        f = perceptron(step, w, b, (x[k], y[k]))
        if f == 1:
            pyplot.plot([x[k]], [y[k]], "g.")
        else:
            pyplot.plot([x[k]], [y[k]], "r.")

num = int(sys.argv[1])
lambd = float(sys.argv[2])

tt = truth_table(2, num)
train(tt, 2, lambd)