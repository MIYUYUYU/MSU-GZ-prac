import math
import itertools

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
        self.x1, self.y1 = float(a[0]), float(a[1])
        self.x2, self.y2 = float(b[0]), float(b[1])
        self.x3, self.y3 = float(c[0]), float(c[1])
        self.a = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
        self.b = math.sqrt((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2)
        self.c = math.sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)

    def __abs__(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        else:
            s = (self.a + self.b + self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def __bool__(self):
        return True if abs(self) else False

    def __lt__(self, other):
        return True if abs(self) < abs(other) else False

    def __contains__(self, other):
        if self.point_in_self(other.x1, other.y1) and self.point_in_self(other.x2, other.y2) and self.point_in_self(other.x3, other.y3) or not bool(other):
            #print(f'{(other.x1,other.y1)}{(other.x2,other.y2)}{(other.x3,other.y3)}{bool(other)}')
            #print(self.point_in_self(other.x1, other.y1) and self.point_in_self(other.x2, other.y2) and self.point_in_self(other.x3, other.y3) and bool(other))
            return True
        else:
            #print(f'{(other.x1, other.y1)}{(other.x2, other.y2)}{(other.x3, other.y3)}{bool(other)}')
            return False

    def __and__(self, other):
        if abs(self) == 0 or abs(other) == 0:
            return False
        else:
            if self in other or other in self:
                return True
            else:
                for a, b in itertools.product(self.get_edges(), other.get_edges()):
                    if cross_two_line(a[0],a[1],b[0],b[1]):
                        return True
                return False

    def point_in_self(self, x, y):
        #判断点是否自己体内，边界也算作在体内
        v1 = (self.x1 - x, self.y1 - y)
        v2 = (self.x2 - x, self.y2 - y)
        v3 = (self.x3 - x, self.y3 - y)
        if math.isclose(modulo(v1[0], v1[1])*modulo(v2[0], v2[1]) * modulo(v3[0], v3[1]),0):
            return True
        alpha1 = (v1[0] * v2[0] + v1[1] * v2[1])/(math.sqrt(v1[0]**2 + v1[1]**2))/(math.sqrt(v2[0]**2 + v2[1]**2))
        alpha2 = (v2[0] * v3[0] + v2[1] * v3[1])/(math.sqrt(v2[0]**2 + v2[1]**2))/(math.sqrt(v3[0]**2 + v3[1]**2))
        alpha3 = (v1[0] * v3[0] + v1[1] * v3[1]) / (math.sqrt(v1[0] ** 2 + v1[1] ** 2)) / (math.sqrt(v3[0] ** 2 + v3[1] ** 2))
        total = (math.acos(alpha1) + math.acos(alpha2) + math.acos(alpha3))/math.pi*180
        #print(f"v1={v1}\nv2={v2}\nv3={v3}\na1: {alpha1} a2:{alpha2} a3:{alpha3} total: {round(total,3)}, self: {abs(self)}")
        if math.isclose(round(total,3), 360):
            return True
        else:
            return False

    def get_edges(self):
        edges = [((self.x1,self.y1),(self.x2,self.y2)),
                 ((self.x1,self.y1),(self.x3,self.y3)),
                 ((self.x2,self.y2),(self.x3,self.y3))]
        return edges

import sys
inp = sys.stdin.read()
exec(inp)


