class Undead(Exception):
    def __init__(self, value):
        super().__init__(value)

class Skeleton(Undead):
    def __init__(self):
        super().__init__("Skeleton")


class Zombie(Undead):
    def __init__(self):
        super().__init__("Zombie")


class Ghoul(Undead):
    def __init__(self):
        super().__init__("Generic Undead")


def necro(a):
    if a % 3 == 0:
        raise Skeleton()
    elif a % 3 == 1:
        raise Zombie()
    elif a % 3 == 2:
        raise Ghoul()

inp = [int(x) for x in input().split(', ')]

for i in range(inp[0],inp[1]):
    try:
        necro(i)
    except Skeleton as e:
        print(e)
    except Zombie as e:
        print(e)
    except Ghoul as e:
        print(e)