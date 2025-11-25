class Doubleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = [super().__call__(*args, **kwargs), super().__call__(*args, **kwargs),2]
        else:
            cls._instances[cls][2] += 1
        return cls._instances[cls][cls._instances[cls][2]%2]

class C(metaclass=Doubleton):
    pass

print(*(C() for i in range(7)), sep="\n")
