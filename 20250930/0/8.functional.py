from math import *
# def MINF(*funs):
#     def fun(x):
#         return min([f(x) for f in funs])
#     return fun
#     return f
#
MINF = lambda *func: lambda x : min([f(x) for f in func])
print(MINF(sin,cos,tan)(1))