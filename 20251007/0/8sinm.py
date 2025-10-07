from math import sin
def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

def out(screen):
    print("\n".join("".join(line) for line in screen))

W, H = eval(input())
A, B = eval(input())
screen = [[' ']*W for i in range(H)]
for i in range(0, W):
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    k = round(scale(-1, 1, 0, H-1, y))
    screen[k][i] = '*'
out(screen)

