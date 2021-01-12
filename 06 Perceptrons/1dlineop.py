# Aaliya Hussain
# 2nd Period
# 6/2/20

import sys

def one_d_minimize(f, left, right, tolerance):
    if right - left < tolerance:
        return (right+left)/2
    o_trd = left + (right-left)/3
    t_trd = right - (right-left)/3
    if f(o_trd) < f(t_trd):
        return one_d_minimize(f, left, t_trd, tolerance)
    else:
        return one_d_minimize(f, o_trd, right, tolerance)

def op_lambd(f, x, y, grad_x, grad_y):
    def one_var(lambd):
        return f(x+lambd*grad_x, y+lambd*grad_y)
    return one_var

def a(x, y):
    return 4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y

def gd_a(x, y):
    return [(8 * x - 3 * y + 24) * -1, (4 * (y - 5) - 3 * x) * -1]

def b(x, y):
    return (1-y)**2 + (x-y**2)**2

def gd_b(x, y):
    return [(2*(x-y**2)) * -1, (2*(-2*x*y+2*y**3+y-1)) * -1]


def graddes_b():
    return one_d_minimize(op_lambd(b, 0, 0, gd_b(0, 0)[0], gd_b(0, 0)[1]), 0, 1, 10**(-8))

coor = [0, 0]
if sys.argv[1] == "A":
    gd_x = gd_a(coor[0], coor[1])[0]
    gd_y = gd_a(coor[0], coor[1])[1]
    while abs(gd_x) > (10 ** (-8)) or abs(gd_y) > (10 ** (-8)):
        lambd = one_d_minimize(op_lambd(a, coor[0], coor[1], gd_x, gd_y), 0, 1, 10**(-8)) #Line Optimization
        print("Current Location: (%s, %s)" % (coor[0], coor[1]))
        print("Current Gradient Vector: (%s, %s)" % (gd_x, gd_y))
        print()
        coor[0] += lambd * gd_x
        coor[1] += lambd * gd_y
        gd_x = gd_a(coor[0], coor[1])[0]
        gd_y = gd_a(coor[0], coor[1])[1]
else:
    gd_x = gd_b(coor[0], coor[1])[0]
    gd_y = gd_b(coor[0], coor[1])[1]
    while abs(gd_x) > (10 ** (-8)) or abs(gd_y) > (10 ** (-8)):
        lambd = one_d_minimize(op_lambd(b, coor[0], coor[1], gd_x, gd_y), 0, 1, 10 ** (-8)) #Line Optimization
        print("Current Location: (%s, %s)" % (coor[0], coor[1]))
        print("Current Gradient Vector: (%s, %s)" % (gd_x, gd_y))
        print()
        coor[0] += lambd * gd_x
        coor[1] += lambd * gd_y
        gd_x = gd_b(coor[0], coor[1])[0]
        gd_y = gd_b(coor[0], coor[1])[1]