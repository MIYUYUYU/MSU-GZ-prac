def gene():
    sum = 0
    i = 1
    while True:
        sum += (1.0 / (i * i))
        yield sum
        i += 1
gen = gene()
for i in range(10):
    print(next(gen))
