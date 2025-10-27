import itertools


def slide(seq, n):
    it = iter(seq)
    it1, it2 = itertools.tee(it)

    while True:
        # 获取当前窗口的n个元素
        window = list(itertools.islice(it1, n))
        if not window:  # 如果窗口为空，结束迭代
            break
        yield from window  # 产生当前窗口的所有元素

        try:
            next(it2)  # 移动窗口：消耗一个元素
        except StopIteration:
            break

        # 为下一轮迭代创建新的tee
        it1, it2 = itertools.tee(it2)

eval(input())