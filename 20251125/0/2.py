class sole(type):
    def __new__(cls, name, bases, attrs):
        if len(bases) > 1:
            raise TypeError("Cannot have more than one parent")
        return super().__new__(cls, name, bases, attrs)

class C(metaclass=sole):
    pass

class D(C):  # 正常
    pass

#以下应该报错
class E(C, int):  # 会抛出TypeError
    pass