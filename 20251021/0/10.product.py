import itertools
from itertools import starmap
a = list(itertools.combinations("qwerty",3))
print(a)
b = list(map(int,starmap(str.__add__,itertools.combinations_with_replacement('0123456789',2))))
print(b)