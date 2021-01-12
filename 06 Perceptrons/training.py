def step(num):
    if num > 0:
        return 1
    return 0

def perceptron(A, w, b, x):
    dot_p = 0
    for e in range(len(w)):
        dot_p += w[e]*x[e]
    return A(dot_p+b)

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

tt1 = [[(1, 1), 0], [(1, 0), 1], [(0, 1), 1], [(0, 0), 1], [(0, -1), 1], [(-1, 0), 1], [(-1, -1), 1], [(-1, 1), 1], [(1, -1), 1]]
vals1 = train(tt1, 2)

tt2 = [[(1, 1), 1], [(1, 0), 1], [(0, 1), 1], [(0, 0), 1], [(0, -1), 1], [(-1, 0), 1], [(-1, -1), 1], [(-1, 1), 1], [(1, -1), 0]]
vals2 = train(tt2, 2)

tt3 = [[(1, 1), 1], [(1, 0), 1], [(0, 1), 1], [(0, 0), 1], [(0, -1), 1], [(-1, 0), 1], [(-1, -1), 0], [(-1, 1), 1], [(1, -1), 1]]
vals3 = train(tt3, 2)

tt4 = [[(1, 1), 1], [(1, 0), 1], [(0, 1), 1], [(0, 0), 1], [(0, -1), 1], [(-1, 0), 1], [(-1, -1), 1], [(-1, 1), 0], [(1, -1), 1]]
vals4 = train(tt4, 2)

print(vals1)
print(vals2)
print(vals3)
print(vals4)