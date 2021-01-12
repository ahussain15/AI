import random
o = [random.randint(0, 3) for k in range(4)]
print(o)
c = 0
cd = {co:o.count(co) for co in o}
for c2 in cd:
    if cd[c2] > 1:
        c += cd[c2]-1
ld = []
for do in range(len(o)):
    ld.append(do+len(o)-1-o[do])
dd = {do:ld.count(do) for do in ld}
for do in dd:
    if dd[do] > 1:
        c += dd[do]-1
rd = []
for do in range(len(o)):
    rd.append(do+o[do])
dd = {do:rd.count(do) for do in rd}
for do in dd:
    if dd[do] > 1:
        c += dd[do]-1
for row in o:
    for col in range(len(o)):
        if col != row:
            print("*", end="  ")
        else:
            print("Q", end="  ")
    print()
print(c)
