import sys


class Vowel:
    __slots__ = ['a', 'o', 'u', 'i', 'e', 'y']
    sorted_slots = sorted(__slots__)
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if name in self.__slots__:
                # 使用 setattr 设置属性
                setattr(self, name, value)

    def __str__(self):
        out = []
        for name in Vowel.sorted_slots:
            if hasattr(self, name):
                out.append(f'{name}: {getattr(self, name)}')
        return ', '.join(out)

    @property
    def full(self):
        return all(hasattr(self, slot) for slot in self.__slots__)
    @full.setter
    def full(self, value):
        pass

    @property
    def answer(self):
        return 42

exec(sys.stdin.read())
