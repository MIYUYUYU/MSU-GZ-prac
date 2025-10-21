import itertools
#print(help(itertools.filterfalse))
seq = [i for i in range(100)]
def divn(n):
    yield from itertools.filterfalse(lambda x: x % n, seq)
a = divn(50)
print(next(a))
print(next(a))