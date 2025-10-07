import decimal
from math import factorial


def esum(N, one):
    E = one
    F = one
    for i in range(1,N+1):
        F *= one / i
        E += one / i
    return E

print(esum(10,1))