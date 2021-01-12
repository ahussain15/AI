# Aaliya Hussain
# 2nd Period
# 4/25/20

import sys, ast, itertools

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
            stable = True
            break
    return cur_w, cur_b, stable

def eval_bit(bits):
    num_f = 2**2**bits
    num_acc = 0
    for f in range(num_f):
        tt = truth_table(bits, f)
        vals = train(tt, bits)
        if vals[2]:
            num_acc += 1
    return num_f, num_acc

# XOR HAPPENS HERE
def xor(A, x):
    # Call to perceptron3 in hidden layer with both inputs
    p3 = perceptron(A, [1, 1], 0, x)
    # Call to perceptron4 in hidden layer with both inputs
    p4 = perceptron(A, [-1, -2], 3, x)
    # Outputs perceptron5 with output of hidden layer as inputs
    return perceptron(A, [1, 2], -2, [p4, p3])


if len(sys.argv) > 2:
    bits = int(sys.argv[1])
    n = int(sys.argv[2])
    tt = truth_table(bits, n)
    vals = train(tt, bits)
    acc = check(tt, vals[0], vals[1])
    print("Final Weight Vector: %s \t Final Bias Value: %s \t Accuracy: %s" % (vals[0], vals[1], acc))
else:
    x = ast.literal_eval(sys.argv[1])
    print("XOR Result: %s" % xor(step, x))