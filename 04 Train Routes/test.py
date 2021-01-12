lats = []
longs = []

with open("rrNodes.txt") as f:
    for line in f:
        data = line.rstrip().split()
        lats.append(float(data[1]))
        longs.append(-1*float(data[2]))

print(sorted(lats)[-1]-sorted(lats)[0])
print(sorted(longs)[-1]-sorted(lats)[0])