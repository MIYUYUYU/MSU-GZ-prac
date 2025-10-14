from collections import Counter
from timeit import Timer

def dcount(words):
    c = {}
    for w in words:
        c[w] = c.get(w, 0) + 1
    return c

def ccount(words):
    return Counter(words)

s = input().split()
td = Timer("dcount(s)", globals = globals())
tc = Timer("ccount(s)", globals = globals())

print("Dict", td.autorange())
print("Counter", tc.autorange())