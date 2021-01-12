# Aaliya Hussain
# 2nd Period
# 3/11/20

import random, sys, math, re

l_to_n = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
n_to_l = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}
let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
gram_freq = dict()


pop_size = 505
clones = 1
tour_size = 20
tour_win = 0.8
xover_pts = 6
mut_rate = 0.8

n_gram = 4
base = 3

# Helper methods
def encode(alphabet):
    cipher = ""
    for l in text:
        if l in l_to_n:
            cipher += alphabet[l_to_n[l]]
    return cipher

def decode(alphabet):
    message = ""
    alpha_i = dict()
    for i in range(len(alphabet)):
        alpha_i[alphabet[i]] = i
    for l in text:
        if l in l_to_n:
            message += n_to_l[alpha_i[l]]
        else:
            message += l
    return message

# Fitness
def store_ngrams():
    with open("ngrams1.tsv") as f:
        start = False
        for line in f:
            info = line.split("\t")
            if info[0] == "".join(str(n_gram)+"-gram"):
                start = True
                continue
            if info[0] == "".join(str(n_gram+1)+"-gram"):
                break
            if start:
                gram_freq[info[0].lower()] = math.log(float(info[1]), base)

store_ngrams()

def fit_score(alphabet):
    total_freq = 0
    decoded = decode(alphabet)
    all_words = re.split("\W+", decoded)
    longer_n = []
    for w in all_words:
        if len(w) >= n_gram:
            longer_n.append(w)
    for w in longer_n:
        for start_i in range(0, len(w)-n_gram+1):
            if w[start_i:start_i+n_gram] in gram_freq:
                total_freq += gram_freq[w[start_i:start_i+n_gram]]
    return total_freq

# Selection
def tournament(pop):
    tourn1 = reversed(sorted([(strat, pop[strat]) for strat in random.sample(pop.keys(), tour_size)], key=lambda x:x[1]))
    tourn2 = reversed(sorted([(strat, pop[strat]) for strat in random.sample(pop.keys(), tour_size)], key=lambda x:x[1]))
    p1 = ""
    p2 = ""
    while p1 == p2 or len(p1) != 26 or len(p2) != 26:
        for p in tourn1:
            if random.random() < tour_win:
                p1 = p[0]
                break
        for p in tourn2:
            if random.random() < tour_win:
                p2 = p[0]
                break
    return p1, p2

# Breeding
def breed(p1, p2):
    ch = ["." for k in range(0, 26)]
    xovers = random.sample(range(0, 26), xover_pts)
    for xpt in xovers:
        ch[xpt] = p1[xpt]
    for rem in range(0, 26):
        if ch[rem] == ".":
            ch[rem] = p2[rem]
        else:
            t = rem
            while ch[t] == ".":
                t += 1
            ch[t] = p2[rem]
    return "".join(ch)

# Mutation
def mutation(ch):
    ch_list = list(ch)
    if random.random() < mut_rate:
        pts = random.sample(range(0, 26), 2)
        ch_list[pts[0]] = ch[pts[1]]
        ch_list[pts[1]] = ch[pts[0]]
    return "".join(ch_list)

# Algorithm
def make_pop(old_pop):
    new_pop = dict()
    clone = find_best(old_pop)
    new_pop[clone] = old_pop[clone]
    while len(new_pop) < pop_size:
        parents = tournament(old_pop)
        ch = mutation(breed(parents[0], parents[1]))
        if ch not in new_pop:
            new_pop[ch] = fit_score(ch)
    return new_pop

def find_best(pop):
    best = ""
    for mem in pop:
        if best == "" or pop[mem] > pop[best]:
            best = mem
    return best


text = sys.argv[1].lower()
cur_pop = dict()
while len(cur_pop) != pop_size:
    mem = "".join(random.sample(let, 26))
    if mem not in cur_pop:
        cur_pop[mem] = fit_score(mem)

for k in range(500):
    print(decode(find_best(cur_pop)).upper())
    cur_pop = make_pop(cur_pop)