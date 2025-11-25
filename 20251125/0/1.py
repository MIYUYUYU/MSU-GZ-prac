C = type('C',(),{'var': 100500, '__init__': lambda self, var : setattr(self, 'var', var)})
print(C.var)
c = C(123)
print(c.var)