def avg_blank_len(board):
    total_len = 0
    num = 0
    for r in range(math.ceil(rows/2)):
        poss = re.finditer("#?[^#]+(?=-)[^#]+#?", board[cols * r:cols * (r + 1)])
        for p in poss:
            if p.group()[0] == "#":
                start = coor_to_index(r, p.start() + 1, cols)
            else:
                start = coor_to_index(r, p.start(), cols)
            if p.group()[-1] == "#":
                end = coor_to_index(r, p.end() - 2, cols)
            else:
                end = coor_to_index(r, p.end() - 1, cols)
            num += 1
            total_len += end-start+1
    for c in range(math.ceil(cols/2)):
        poss = re.finditer("#?[^#]+(?=-)[^#]+#?", board[c:(rows * cols) - (cols - c - 1):cols])
        for p in poss:
            if p.group()[0] == "#":
                start = coor_to_index(p.start() + 1, c, cols)
            else:
                start = coor_to_index(p.start(), c, cols)
            if p.group()[-1] == "#":
                end = coor_to_index(p.end() - 2, c, cols)
            else:
                end = coor_to_index(p.end() - 1, c, cols)
            num += 1
            total_len += int((end-start)/cols)+1
    if num != 0:
        return total_len/num
    return 0