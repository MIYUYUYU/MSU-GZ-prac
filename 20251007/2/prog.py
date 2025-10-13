from math import *

def scale(a, b, A, B, x):
    """将x从区间[a,b]映射到区间[A,B]"""
    return (x - a) * (B - A) / (b - a) + A


def draw_function(W, H, A, B, func_str):
    """绘制函数图形"""
    # 定义函数
    def f(x):
        return eval(func_str,{'x':x},globals())

    # 初始化屏幕
    screen = [[' '] * W for _ in range(H)]

    # 计算所有点的函数值
    y_values = []
    for i in range(W):
        x = scale(0, W - 1, A, B, i)
        y_values.append(f(x))

    # 找到最小和最大值
    y_min = min(y_values)
    y_max = max(y_values)

    # 绘制函数图形
    for i in range(W):
        # 将y值映射到行坐标
        k = round(scale(y_min, y_max, H-1, 0, y_values[i]))

        # 确保在屏幕范围内
        if 0 <= k < H:
            screen[k][i] = '*'
    return screen



data = input().split()
#print(f'data: {data}')
W = int(data[0])
H = int(data[1])
A = float(data[2])
B = float(data[3])
func_str = data[4]

# 绘制函数图形
screen = draw_function(W, H, A, B, func_str)

# 输出结果
print("\n".join("".join(line) for line in screen))

