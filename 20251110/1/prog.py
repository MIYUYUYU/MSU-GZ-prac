import collections
import sys
class DivStr(collections.UserString):
    def __init__(self, value = ''):
        super().__init__(value)
        self._value = super().__str__()
        self._floordiv_index = 0

    def __str__(self):
        return self._value

    def __floordiv__(self, other):
        length = len(self._value) // other
        outlist = []
        for i in range(other):
            row = self._value[i*length:(i+1)*length]
            outlist.append(row)
        self._floordiv_index = length * other
        #print(self._floordiv_index)
        return iter(outlist)

    def __mod__(self, other):
        self.__floordiv__(other)
        #print(self._floordiv_index)
        return DivStr(self._value[self._floordiv_index:])


exec(sys.stdin.read())