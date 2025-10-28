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

    def area(self):
        """area ractangle """
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def __lt__(self, other):
        """<"""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()
