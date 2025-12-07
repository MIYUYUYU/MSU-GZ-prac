import asyncio
import random
import sys

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    """Слияние двух упорядоченных отрезков A1[start:middle] и A1[middle:finish] в A2[start:finish]."""
    await asyncio.gather(event_in1.wait(), event_in2.wait())

    i, j = start, middle
    k = start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()


async def mtasks(A):
    n = len(A)
    # 创建A的副本，用于排序过程
    A_copy = A[:]
    B = [0] * n
    #print(f'{B=}')
    tasks = []

    # 初始事件：每个长度为1的段都已经"排序"好了
    segment_events = [[asyncio.Event() for _ in range(n)]]
    for e in segment_events[0]:
        e.set()

    size = 1
    level = 0

    while size < n:
        prev_events = segment_events[level]
        segment_count = (n + size - 1) // size
        next_events = [asyncio.Event() for _ in range(segment_count + 1 // 2)]

        for i in range(0, segment_count, 2):
            # 确定源数组和目标数组
            if level % 2 == 0:
                src, dst = A_copy, B
            else:
                src, dst = B, A_copy

            if i + 1 < segment_count:
                # 两个段合并
                start = i * size
                middle = min(start + size, n)
                finish = min(start + 2 * size, n)

                task = merge(src, dst, start, middle, finish,
                             prev_events[i], prev_events[i + 1],
                             next_events[i // 2])
                tasks.append(task)
            else:
                # 单个段，需要复制
                start = i * size
                finish = min(start + size, n)

                async def copy_segment(src_arr, dst_arr, s, f, ev_in, ev_out):
                    await ev_in.wait()
                    for idx in range(s, f):
                        dst_arr[idx] = src_arr[idx]
                    ev_out.set()

                # 捕获循环变量的当前值
                task = copy_segment(src, dst, start, finish, prev_events[i], next_events[i // 2])
                tasks.append(task)

        segment_events.append(next_events)
        size *= 2
        level += 1

    # 确定最终结果在哪个数组中
    # 如果总层数为奇数，则最终结果在B中
    # 如果总层数为偶数，则最终结果在A_copy中，需要复制到B
    if level % 2 == 0:
        # 最终结果在A_copy中，需要复制到B
        final_event = segment_events[level][0]  # 最后一个事件

        async def copy_final():
            await final_event.wait()
            for i in range(n):
                B[i] = A_copy[i]

        tasks.append(copy_final())

    return tasks, B


exec(sys.stdin.read())



# async def main(A):
#     tasks, B = await mtasks(A)
#     print(len(tasks))
#     random.shuffle(tasks)
#     await asyncio.gather(*tasks)
#     return B
#
#
# random.seed(1333)
# A = random.choices(range(10), k=25)
# B = asyncio.run(main(A))
# print(*A)
# print(*B)
# print(B == sorted(A))