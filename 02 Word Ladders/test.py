def is_next(w1, w2):
    d = 0
    if abs(len(w1)-len(w2)) > 1:
        return False
    if len(w1) == len(w2):
        for x in range(0, len(w1)):
            if w1[x] != w2[x]:
                d += 1
                if d > 1:
                    return False
    if len(w1)-len(w2) == 1:
         x2 = 0
         for x in range(0, len(w2)):
             if sorted(w2)[x] != sorted(w1)[x2]:
                 d += 1
                 if d > 1:
                     return False
                 continue
             x2 += 1
    if len(w1)-len(w2) == -1:
        x2 = 0
        for x in range(0, len(w1)):
            if sorted(w2)[x2] != sorted(w1)[x]:
                d += 1
                if d > 1:
                    return False
                continue
            x2 += 1
    return True