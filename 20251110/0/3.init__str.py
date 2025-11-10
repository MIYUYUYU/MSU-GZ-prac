C = type('CC',(),{'a':213,'__str__': lambda self: f'{self.__class__.__name__}','#a13d1q' : (123)})
c = C()
print(c.a)
print(c)
print(C.__dict__['#a13d1q'])
D = type('DD',(),{'__init__': lambda self, val: setattr(self.__class__,'Q-Q!',val),
                  '__str__':lambda self: f'<{self.__class__.__dict__['Q-Q!']}>'})
d = D(123)
print(d)