class A:
    def __str__(self):
        return 'A'

class B(A):
    def __str__(self):
        return super().__str__() + f':B'

class C(B):
    def __str__(self):
        return super().__str__() + f':C'

print(B())
print(C())
