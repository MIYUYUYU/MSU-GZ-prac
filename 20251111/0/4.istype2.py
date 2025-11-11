class IsType:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, f):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, self.typ):
                    raise TypeError(f"All arguments must be {self.typ}, got {type(arg)}")
            return f(*args)

        return wrapper


@IsType(int)
def fun(a, b):
    return a * 2 + b


print(fun(2, 3))  # Работает
# print(fun(2, "3"))  # TypeError