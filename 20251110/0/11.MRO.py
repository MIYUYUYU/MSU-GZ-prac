import itertools

class A:pass
class B:pass
class C(A, B):pass
class D(B, A):pass

class E(A, B):pass
#class E1(A, C):pass
#class E2(A, D):pass
#class E3(C, D):pass
#class E4(B, C):pass
#class E5(B, D):pass
H = itertools.product("ABCD","ABCD")
#I = itertools.product("ABCD","DCBA")
#print(list(H))
count = 16
for a in list(H):
    try:
        class E(a[0],a[1]): pass
    except Exception:
        count -= 1
    else:
        print(a[0],a[1])