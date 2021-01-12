# Aaliya Hussain
# 2nd Period
# 5/16/20

import sys, numpy, math, random

def sigmoid(x):
    return 1 / (1 + math.exp(-1 * x))

# SUM
def sum_backprop(A, x_list, y_list, w_list, b_list, lambd):
    v_A = numpy.vectorize(A)
    n_w_list = w_list
    n_b_list = b_list
    for e in range(500):
        print("Epoch: %s" % (e+1))
        lambd = lambd*0.99998
        for pair in range(len(x_list)):
            n = len(w_list) - 1
            a_list = [x_list[pair]]
            dot_list = [None]
            delta_list = [None for k in range(n+1)]
            for l in range(1, n+1):
                dot_list.append(a_list[l-1]@n_w_list[l]+n_b_list[l])
                a_list.append(v_A(dot_list[l]))
            delta_list[n] = (v_A(dot_list[n])*(1-v_A(dot_list[n])))*(y_list[pair]-a_list[n])
            for l in range(n-1, 0, -1):
                delta_list[l] = (v_A(dot_list[l])*(1-v_A(dot_list[l])))*(delta_list[l+1]@n_w_list[l+1].transpose())
            for l in range(1, n+1):
                n_w_list[l] = n_w_list[l]+lambd*a_list[l-1].transpose()@delta_list[l]
                n_b_list[l] = n_b_list[l]+lambd*delta_list[l]
            print(a_list[n])

w_l_s = [None, 2 * numpy.random.rand(2, 2) - 1, 2 * numpy.random.rand(2, 2) - 1]
b_l_s = [None, 2 * numpy.random.rand(1, 2) - 1, 2 * numpy.random.rand(1, 2) - 1]
x_l_s = [numpy.array([[0, 0]]), numpy.array([[0, 1]]), numpy.array([[1, 0]]), numpy.array([[1, 1]])]
y_l_s = [numpy.array([[0, 0]]), numpy.array([[0, 1]]), numpy.array([[0, 1]]), numpy.array([[1, 0]])]

# CIRCLE
def circle_backprop(A, x_list, y_list, w_list, b_list, lambd):
    v_A = numpy.vectorize(A)
    n_w_list = w_list
    n_b_list = b_list
    for pair in range(len(x_list)):
        n = len(w_list) - 1
        a_list = [x_list[pair]]
        dot_list = [None]
        delta_list = [None for k in range(n+1)]
        for l in range(1, n+1):
            dot_list.append(a_list[l-1]@n_w_list[l]+n_b_list[l])
            a_list.append(v_A(dot_list[l]))
        delta_list[n] = (v_A(dot_list[n])*(1-v_A(dot_list[n])))*(y_list[pair]-a_list[n])
        for l in range(n-1, 0, -1):
            delta_list[l] = (v_A(dot_list[l])*(1-v_A(dot_list[l])))*(delta_list[l+1]@n_w_list[l+1].transpose())
        for l in range(1, n+1):
            n_w_list[l] = n_w_list[l]+lambd*a_list[l-1].transpose()@delta_list[l]
            n_b_list[l] = n_b_list[l]+lambd*delta_list[l]
    return n_w_list, n_b_list

def p_net(A, x_list, y_list, w_list, b_list):
    v_A = numpy.vectorize(A)
    wrong = 0
    error = 0
    for x in range(len(x_list)):
        a_l = x_list[x]
        for l in range(1, len(w_list)):
            a_l = v_A(a_l@w_list[l]+b_list[l])
        error += abs(a_l[0][0] - y_list[x][0])
        if round(a_l[0][0]) != y_list[x][0]:
            wrong += 1
    return wrong, error

def in_circle(x, y):
    if (x**2+y**2)**0.5 <= 1:
        return 1
    return 0

def gen_10K():
    x = [numpy.array([(random.uniform(-1, 1), random.uniform(-1, 1))]) for k in range(10000)]
    y = []
    for p in x:
        y.append(numpy.array([in_circle(p[0][0], p[0][1])]))
    return x, y

def circle():
    w_l_c = [None, 2 * numpy.random.rand(2, 12) - 1, 2 * numpy.random.rand(12, 4) - 1, 2 * numpy.random.rand(4, 1) - 1]
    b_l_c = [None, 2 * numpy.random.rand(1, 12) - 1, 2 * numpy.random.rand(1, 4) - 1, 2 * numpy.random.rand(1, 1) - 1]
    data = gen_10K()
    x_l_c = data[0]
    y_l_c = data[1]
    lambd = p_net(sigmoid, x_l_c, y_l_c, w_l_c, b_l_c)[1]/10000
    for e in range(500):
        print("Epoch: %s" % (e+1))
        train = circle_backprop(sigmoid, x_l_c, y_l_c, w_l_c, b_l_c, lambd)
        w_l_c = train[0]
        b_l_c = train[1]
        current = p_net(sigmoid, x_l_c, y_l_c, w_l_c, b_l_c)
        wrong = current[0]
        lambd = current[1]/10000
        print("Number of points misclassified: %s" % wrong)

if sys.argv[1] == "S":
    sum_backprop(sigmoid, x_l_s, y_l_s, w_l_s, b_l_s, 10)
else:
    circle()