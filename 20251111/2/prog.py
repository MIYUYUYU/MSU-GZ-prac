import sys
class Num:
    def __init__(self, i = 0):
        self.default = i
        self.num = {}

    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            self.num[obj] = value
        elif hasattr(value, '__len__'):
            self.num[obj] = len(value)

    def __get__(self, instance, owner=None):
        # print(self)
        # print(value)
        if instance is not None:
            return self.num.get(instance, self.default)
        else:
            return self.default


    def __add__(self, other):
        return Num(self.num[self] + other.num[other])

    def __str__(self):
        return self.default

exec(sys.stdin.read())