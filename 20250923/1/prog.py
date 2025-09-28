x = eval(input())
print([n for n in range(x[0], x[1]) if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))])