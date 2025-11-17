import math
import itertools
class InvalidInput(Exception):
    def __init__(self):
        super().__init__("Invalid input")

    def __str__(self):
        return "Invalid input"

class BadTriangle(Exception):
    def __init__(self):
        super().__init__("Not a triangle")

    def __str__(self):
        return "Not a triangle"

def modulo(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def cross(o:tuple, a:tuple, b:tuple):
    oa = (a[0]-o[0], a[1]-o[1])
    ob = (b[0]-o[0], b[1]-o[1])
    return oa[0] * ob[1] - oa[1] * ob[0]

def dot(o:tuple, a:tuple, b:tuple):
    oa = (o[0]-a[0], o[1]-a[1])
    ob = (b[0]-a[0], b[1]-a[1])
    return oa[0] * ob[0] + oa[1] * ob[1]

def cross_two_line(base_x:tuple, base_y, target_x, target_y):
    con1_1 = round(cross(base_x, base_y, target_x),3) #判断tx和ty点是否位于bx,by点两侧
    con1_2 = round(cross(base_x, base_y, target_y),3)
    con2_1 = round(cross(target_x, target_y, base_x),3)
    con2_2 = round(cross(target_x, target_y, base_y),3)
    if con1_1 * con1_2 < 0 and con2_1 * con2_2 < 0:
        return True
    elif con1_1 == 0 and round(dot(target_x, base_x, base_y),3) <= 0:
        return True
    elif con1_2 == 0 and round(dot(target_y, base_x, base_y),3) <= 0:
        return True
    elif con2_1 == 0 and round(dot(base_x, target_x, target_y),3) <= 0:
        return True
    elif con2_2 == 0 and round(dot(base_y, target_x, target_y),3) <= 0:
        return True
    return False

class Triangle:
    def __init__(self, a, b, c):
        if (type(a) != tuple or type(b) != tuple or type(c) != tuple or not hasattr(a, '__getitem__')
                or not hasattr(b, '__getitem__') or not hasattr(c, '__getitem__')):
            raise InvalidInput()
        self.x1, self.y1 = float(a[0]), float(a[1])
        self.x2, self.y2 = float(b[0]), float(b[1])
        self.x3, self.y3 = float(c[0]), float(c[1])
        self.a = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
        self.b = math.sqrt((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2)
        self.c = math.sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)

    def __abs__(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise BadTriangle()
        else:
            s = (self.a + self.b + self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

def inputTriangle():
    while True:
        try:
            inp = [eval(x) for x in input().split(", ")]
        except EOFError:
            break
        except Exception:
            print("Invalid input")
            continue
        try:
            tri = Triangle(inp[0], inp[1], inp[2])
        except InvalidInput as e:
            print(e)
        except BadTriangle as e:
            print(e)
        except Exception:
            print("Invalid input")
            continue
        else:
            try:
                print(f'{round(abs(tri)):.2f}')
            except BadTriangle as e:
                print(e)
                continue
            else:
                break

inputTriangle()
#print(dir(Exception))
# import sys
# inp = sys.stdin.read()
# exec(inp)


