globals()["A"] = 'abc'
print(eval("a + b",{'b': 123,'a':456}))
#print(dir(__builtins__))
