class E1(Exception):
    pass

class E2(Exception):
    pass

class E3(E2):
    pass

for i in [Exception(), E1(), E2(), E3()]:
    try:
        raise i
    except E3:
        print('E3')
    except E2:
        print('E2')
    except E1:
        print('E1')
    except Exception:
        print("EEEE")

print()


for i in [Exception(), E1(), E2(), E3()]:
    try:
        raise i
    except E3:
        print('E3')
    except E2:
        print('E2')
    except Exception:
        print("EEEE")
    except E1:
        print('E1')

