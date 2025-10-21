from itertools import product
from itertools import starmap
dosk = product("abcdefgh","12345678")
b= list(starmap(str.__add__,dosk))
print(*("".join(name) for name in b))