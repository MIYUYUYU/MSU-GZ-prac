def istype(typ):
    def decorator(f):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, typ):
                    raise TypeError(f"All arguments must be {typ}, got {type(arg)}")
            return f(*args)
        return wrapper
    return decorator

@istype(int)
def fun1(a, b):
    return a * 2 + b

@istype(str)
def fun2(a, b):
    return a + b

print(fun1(2, 3))    # Работает
print(fun2("a", "b")) # Работает
# print(fun1(2, "3")) # TypeError