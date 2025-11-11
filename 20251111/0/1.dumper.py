def dumper(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun


@dumper
def fun(a, b):
    return a * 2 + b


print(fun(2, 3))