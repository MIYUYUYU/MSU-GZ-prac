def isint(f):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"All arguments must be int, got {type(arg)}")
        return f(*args)
    return wrapper

@isint
def fun(a, b):
    return a * 2 + b

# Тестирование
print(fun(2, 3))  # Работает
# print(fun(2, "3"))  # Вызовет TypeError