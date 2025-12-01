import sys

class dump(type):
    def __new__(mcs, name, bases, attrs):
        # 遍历类的所有属性
        for attr_name, attr_value in attrs.items():
            # 只处理可调用的方法（函数），排除魔法方法如__new__, __prepare__等（可选）
            # 这里根据题目要求，处理所有方法，包括__init__
            if callable(attr_value):
                # 包装方法
                attrs[attr_name] = mcs.wrap_method(attr_name, attr_value)

        # 使用修改后的属性创建新类
        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def wrap_method(method_name, method):
        """
        包装方法，添加参数打印功能
        """

        def wrapper(self, *args, **kwargs):
            # 打印方法名和参数
            print(f"{method_name}: {args}, {kwargs}")
            # 调用原始方法
            return method(self, *args, **kwargs)

        return wrapper


class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)


exec(sys.stdin.read())