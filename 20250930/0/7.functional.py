def f(x):
    return x * 2
def g(x):
    return x * 3 + 1
def F(fun1, fun2):
    def fun(x):
        return fun1(x) + fun2(x)
    return fun

print(f(2))
print(g(2))
s = F(f, g)
print(s(2))
print(s.__closure__)