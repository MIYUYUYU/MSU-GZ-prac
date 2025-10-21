import itertools
from itertools import starmap
def repeater(seq, n):
    for i in range(n):
        yield from seq

print(list(repeater("QWE",3)))
a, b, c = map(float, input().split())
print(a,b,c)
a, b, c = starmap(int,(("123123",4),("deadbeef",16),("1000",10)))
print(a, b, c)