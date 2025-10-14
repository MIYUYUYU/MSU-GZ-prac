from string import ascii_lowercase
from timeit import Timer

wov = set("aouie")
con = set(ascii_lowercase) - wov

def wovcon(s):
    return len(s & wov), len(s & con)

s = set(input())
T = Timer("wovcon(s)", globals=globals())
res = T.autorange()
print(res)