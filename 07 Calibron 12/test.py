def get_next_var(l):
    return rect_list[len(l)]


def get_sorted_vals(l, var):
    poss = []
    rw = max(var[0], var[1])
    rh = min(var[0], var[1])
    for x in range(puzzle_width):
        for y in range(puzzle_height):
            addH = True
            if x + rw > puzzle_width or y + rh > puzzle_height:
                addH = False
            else:
                for ap in l:
                    if (x == ap[0] and y == ap[1]) or (
                            ((x >= ap[0] and x + rw <= ap[0] + ap[2]) or (ap[0] >= x and ap[0] + ap[2] <= x + rw)) and (
                            (y >= ap[1] and y + rh <= ap[1] + ap[3]) or (ap[1] >= y and ap[1] + ap[3] <= y + rh))):
                        addH = False
                        break
            if addH:
                poss.append((x, y, rw, rh))
            if rh != rw:
                addV = True
                if x + rh > puzzle_width or y + rw > puzzle_height:
                    addV = False
                else:
                    for ap in l:
                        if (x == ap[0] and y == ap[1]) or (((x >= ap[0] and x + rh <= ap[0] + ap[2]) or (
                                ap[0] >= x and ap[0] + ap[2] <= x + rh)) and (
                                                                   (y >= ap[1] and y + rw <= ap[1] + ap[3]) or (
                                                                   ap[1] >= y and ap[1] + ap[3] <= y + rw))):
                            addV = False
                            break
                if addV:
                    poss.append((x, y, rh, rw))
    return poss
