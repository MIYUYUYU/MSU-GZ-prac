class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.__class__(self.val + other.val)
    def __str__(self):
        return f"<{self.val}>"

class B(A):
    def __str__(self):
        return f'>{self.val}<'

a = A(3)
b = B(4)
print(a)

print(b+a)
print(b)