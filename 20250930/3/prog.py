from math import *

s, t, u = eval(input())
#print(f"s = {s} t = {t} u = {u}")
x_val = eval(input())
def Calc(s, t, u):
    def inner(x):
        x = x_val
        s_result = eval(s,{'x': x},globals())
        t_result = eval(t,{'x': x},globals())

        x = s_result
        y = t_result
        u_result = eval(u,{'x': x, 'y': y},globals())
        return u_result
    return inner
calc_x = Calc(s, t, u)
print(calc_x(x_val))