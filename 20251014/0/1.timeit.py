from timeit import *
code = input()
timer = Timer(stmt=code)
result = timer.autorange()
print(result[1] / result[0])


class Timer:
    pass