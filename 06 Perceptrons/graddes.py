# Aaliya Hussain
# 2nd Period
# 5/10/20

import sys

def a():
    lambd = 0.001
    coor = [0, 0]
    grad_x = (8*coor[0] - 3*coor[1] + 24)*-1
    grad_y = (4*(coor[1] - 5) - 3*coor[0])*-1
    while abs(grad_x) > (10**(-8)) or abs(grad_y) > (10**(-8)):
        print("Current Location: (%s, %s)" % (coor[0], coor[1]))
        print("Current Gradient Vector: (%s, %s)" % (grad_x, grad_y))
        print()
        coor[0] += lambd*grad_x
        coor[1] += lambd*grad_y
        grad_x = (8 * coor[0] - 3 * coor[1] + 24) * -1
        grad_y = (4 * (coor[1] - 5) - 3 * coor[0]) * -1

def b():
    lambd = 0.001
    coor = [0, 0]
    grad_x = (2*(coor[0]-coor[1]**2)) * -1
    grad_y = (2*(-2*coor[0]*coor[1]+2*coor[1]**3+coor[1]-1)) * -1
    while abs(grad_x) > (10 ** (-8)) or abs(grad_y) > (10 ** (-8)):
        print("Current Location: (%s, %s)" % (coor[0], coor[1]))
        print("Current Gradient Vector: (%s, %s)" % (grad_x, grad_y))
        print()
        coor[0] += lambd * grad_x
        coor[1] += lambd * grad_y
        grad_x = (2 * (coor[0] - coor[1] ** 2)) * -1
        grad_y = (2 * (-2 * coor[0] * coor[1] + 2 * coor[1] ** 3 + coor[1] - 1)) * -1

a()

# if sys.argv[1] == "A":
#     a()
# else:
#     b()