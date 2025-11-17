import sys
def objcount(cls):
    class ObjCount(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            ObjCount.counter += 1
        def __del__(self):
            ObjCount.counter -= 1
            
    return ObjCount

exec(sys.stdin.read())


