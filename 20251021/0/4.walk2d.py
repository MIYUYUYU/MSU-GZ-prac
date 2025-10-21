def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy

a = walk2d()
a.send(None)
print(a.send((1,2)))
print(a.send((-1,-2)))
print(a.send((-1,-5)))