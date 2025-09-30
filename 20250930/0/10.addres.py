def gen_adders(n):
    adders = []
    for i in range(n):
        def fun(x, y = i):
            return x + y
        adders.append(fun)
    del i
    return adders
ad = gen_adders(5)
print(ad[2](100), ad[0](100))
print(ad[0].__closure__)
print(ad[1].__closure__)
#print(ad[2].__closure__[0].cell_contents)