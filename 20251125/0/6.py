class AnnotatedClass:
    a: int

    def __init__(self, val):
        if not isinstance(val, self.__annotations__['a']):
            raise TypeError(f"Expected {self.__annotations__['a']}, got {type(val)}")
        self.a = val
obj1 = AnnotatedClass(5)   # 正常
#obj2 = AnnotatedClass("5") # 抛出TypeError

import inspect

print(AnnotatedClass.__annotations__)
print(inspect.get_annotations(AnnotatedClass))