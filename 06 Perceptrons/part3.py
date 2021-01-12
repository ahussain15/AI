# Aaliya Hussain
# 2nd Period
# 5/12/20

import numpy, sys, ast, math, random

def step(num):
    if num > 0:
        return 1
    return 0

def p_net(A, x, w_list, b_list):
    v_A = numpy.vectorize(A)
    a_l = x
    for l in range(len(w_list)):
        a_l = v_A(a_l@w_list[l]+b_list[l])
    return a_l[0]

# XOR HAPPENS HERE
x_w = [numpy.array(([1, -1], [1, -2])), numpy.array(([1], [2]))]
x_b = [numpy.array(([0, 3])), numpy.array(([-2]))]

# Diamond
d_w = [numpy.array(([-1, 1, 1, -1], [-1, -1, 1, 1])), numpy.array(([1], [2], [3], [4]))]
d_b = [numpy.array(([1, 1, 1, 1])), numpy.array(([-9]))]

# Circle
c_w = [numpy.array(([-1, 1, 1, -1], [-1, -1, 1, 1])), numpy.array(([1], [2], [3], [4]))]
c_b = [numpy.array(([1.41, 1.35, 1.35, 5.15])), numpy.array(([-8.0552]))]

def sigmoid(x):
    return 1 / (1 + math.exp(-1*x))

def in_circle(x, y):
    if (x**2+y**2)**0.5 <= 1:
        return 1
    return 0

def gen_500():
    points = [[(random.uniform(-1, 1), random.uniform(-1, 1))] for k in range(500)]
    for p in points:
        p.append(in_circle(p[0][0], p[0][1]))
    return points

def check(A, points, w_list, b_list):
    right = 0
    wrong = []
    for p in points:
        comp = round(p_net(A, p[0], w_list, b_list))
        if comp == p[1]:
            right += 1
        else:
            wrong.append(p[0])
    return right/5, wrong

if len(sys.argv) == 2:
    x = ast.literal_eval(sys.argv[1])
    print("XOR Result: %s" % p_net(step, x, x_w, x_b))
if len(sys.argv) == 3:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    d = p_net(step, (x, y), d_w, d_b)
    if d == 0:
        print("Outside")
    else:
        print("Inside")
if len(sys.argv) == 1:
    points = gen_500()
    results = check(sigmoid, points, c_w, c_b)
    print("Percentage Correct: %s" % results[0])
    print("Misclassified Points: %s" % results[1])
