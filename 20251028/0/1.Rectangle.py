class Rectangle:
    def __init__(self,x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2,self.y2})({self.x2,self.y1})"


rect1 = Rectangle(0, 0, 5, 3)
rect2 = Rectangle(1, 1, 4, 6)

# 测试字符串表示
print("矩形1:", rect1)
print("矩形2:", rect2)

# 验证坐标
print(f"矩形1坐标: x1={rect1.x1}, y1={rect1.y1}, x2={rect1.x2}, y2={rect1.y2}")
print(f"矩形2坐标: x1={rect2.x1}, y1={rect2.y1}, x2={rect2.x2}, y2={rect2.y2}")