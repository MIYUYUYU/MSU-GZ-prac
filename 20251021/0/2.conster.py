def gene():
    total = 0
    i = 1
    while True:
        total += (1.0 / (i * i))
        yield total
        i += 1
gen = gene()
print(sum([next(gen) for i in range(10000)]))

