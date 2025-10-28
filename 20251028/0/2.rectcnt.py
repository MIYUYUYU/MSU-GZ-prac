class Rectangle:
    rectcnt = 0
    def __init__(self,x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        Rectangle.rectcnt += 1
    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2,self.y2})({self.x2,self.y1})"


print(f"count before creation: {Rectangle.rectcnt}")

# 创建多个矩形对象
rects = []
for i in range(5):
    rect = Rectangle(i, i, i + 2, i + 3)
    rects.append(rect)
    print(rect)  # 打印每个矩形，包含计数器值
    print(f"current count: {Rectangle.rectcnt}")  # 验证计数器

# 最终验证
print(f"всего создал {len(rects)} объектов, count: {Rectangle.rectcnt}")