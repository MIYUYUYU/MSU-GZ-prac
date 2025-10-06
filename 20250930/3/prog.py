from math import *


def Calc(s, t, u):
    # 返回一个新函数，该函数计算 u(s(x), t(x))
    return lambda x: eval(u, globals(), {'x': eval(s, globals(), {'x': x}),
                                         'y': eval(t, globals(), {'x': x})})


def main():
    # 读取三个公式字符串
    formulas = eval(input().strip())
    s, t, u = formulas

    # 读取 x 值
    x_val = eval(input().strip())

    # 创建计算函数并计算结果
    F = Calc(s, t, u)
    result = F(x_val)
    print(result)


if __name__ == '__main__':
    main()