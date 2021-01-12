# Aaliya Hussain
# 2nd Period
# 4-15-20

import sys, ast, itertools

def truth_table(bits, n):
    table = [[tuple(vs)] for vs in itertools.product([1, 0], repeat=bits)]
    bin_rep = bin(n)[2:]
    for i in range(len(table)-len(bin_rep), len(table)):
        table[i].append(int(bin_rep[i-len(bin_rep)]))
    for i in range(0, len(table)-len(bin_rep)):
        table[i].append(0)
    return table

def pretty_print_tt(table):
    header = []
    bits = len(table[0][0])
    for b in range(bits):
        header.append("Col %s \t" % (b+1))
    header.append("Out")
    print("".join(header))
    for r in range(len(table)):
        row = []
        for b in range(bits):
            row.append(str(table[r][0][b])+"\t"+"\t")
        row.append(str(table[r][1]))
        print("".join(row))

def step(num):
    if num > 0:
        return 1
    return 0

def perceptron(A, w, b, x):
    dot_p = 0
    for e in range(len(w)):
        dot_p += w[e]*x[e]
    return A(dot_p+b)

def check(n, w, b):
    tt = truth_table(len(w), n)
    right = 0
    for i in range(len(tt)):
        p = perceptron(step, w, b, tt[i][0])
        if p == tt[i][1]:
            right += 1
    return right/len(tt)

n = int(sys.argv[1])
w = ast.literal_eval(sys.argv[2])
b = float(sys.argv[3])
print(check(n, w, b))