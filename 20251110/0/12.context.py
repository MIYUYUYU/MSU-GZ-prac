import sys
try:
    try:
        1/0
    except Exception as e:
        print(e.arg)
except Exception as q:
    print(q.args)
    print(q.__context__)
    print(q.__cause__)
