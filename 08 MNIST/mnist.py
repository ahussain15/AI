# Aaliya Hussain
# 2nd Period
# 5/19/20

import csv, numpy, math, pickle

def pickle_training():
    output_lists = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    x_list = []
    y_list = []
    with open("mnist_train.csv") as file:
        tr = csv.reader(file, delimiter=",")
        for line in tr:
            y_list.append(numpy.array(output_lists[int(line[0])]))
            x = []
            for p in range(1, len(line)):
                x.append(float(line[p])/255)
            x_list.append(numpy.array([x]))
    x_file = open("training_x", "wb")
    pickle.dump(x_list, x_file)
    x_file.close()
    y_file = open("training_y", "wb")
    pickle.dump(y_list, y_file)
    y_file.close()

def pickle_test():
    output_lists = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    x_list = []
    y_list = []
    with open("mnist_test.csv") as file:
        tr = csv.reader(file, delimiter=",")
        for line in tr:
            y_list.append(numpy.array(output_lists[int(line[0])]))
            x = []
            for p in range(1, len(line)):
                x.append(float(line[p])/255)
            x_list.append(numpy.array([x]))
    x_file = open("test_x", "wb")
    pickle.dump(x_list, x_file)
    x_file.close()
    y_file = open("test_y", "wb")
    pickle.dump(y_list, y_file)
    y_file.close()

x_file_tr = open("training_x", "rb")
x_list_tr = pickle.load(x_file_tr)
x_file_tr.close()
y_file_tr = open("training_y", "rb")
y_list_tr = pickle.load(y_file_tr)
y_file_tr.close()

x_file_te = open("test_x", "rb")
x_list_te = pickle.load(x_file_te)
x_file_te.close()
y_file_te = open("test_y", "rb")
y_list_te = pickle.load(y_file_te)
y_file_te.close()

def gen_network(nodes):
    w_list = [None]
    b_list = [None]
    for n in range(1, len(nodes)):
        w_list.append(2 * numpy.random.rand(nodes[n-1], nodes[n]) - 1)
        b_list.append(2 * numpy.random.rand(1, nodes[n]) - 1)
    return w_list, b_list

def sigmoid(x):
    return 1 / (1 + math.exp(-1 * x))

def backprop(A, x_list, y_list, w_list, b_list, lambd):
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
    w_file = open("latest_w", "wb")
    pickle.dump(n_w_list, w_file)
    w_file.close()
    b_file = open("latest_b", "wb")
    pickle.dump(n_b_list, b_file)
    b_file.close()

def p_net(A, x_list, y_list, w_list, b_list):
    v_A = numpy.vectorize(A)
    wrong = 0
    for x in range(len(x_list)):
        a_l = x_list[x]
        for l in range(1, len(w_list)):
            a_l = v_A(a_l@w_list[l]+b_list[l])
        if list(a_l[0]).index(max(a_l[0])) != list(y_list[x]).index(max(y_list[x])):
            wrong += 1
    return wrong/len(y_list)

# Start
start = gen_network([784, 300, 100, 10])
print("Network Architecture: %s" % [784, 300, 100, 10])
w_list = start[0]
b_list = start[1]
backprop(sigmoid, x_list_tr, y_list_tr, w_list, b_list, 1)

for e in range(1, 6):
    w_file = open("latest_w", "rb")
    w_list = pickle.load(w_file)
    w_file.close()
    b_file = open("latest_b", "rb")
    b_list = pickle.load(b_file)
    b_file.close()
    print("Epoch %s:" % e)
    result = p_net(sigmoid, x_list_te, y_list_te, w_list, b_list)
    print("%s percent misclassified" % (result*100))
    backprop(sigmoid, x_list_tr, y_list_tr, w_list, b_list, 0.1)