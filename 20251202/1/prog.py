import asyncio
import sys
async def writer(queue, delay, stop_event):
    i = 0
    #await asyncio.sleep(delay)
    while not stop_event.is_set():
        #print(stop_event.is_set())
        item = f'{i}_{delay}'
        await queue.put(item)
        await asyncio.sleep(delay)
        i += 1


async def stacker(source_queue, dest_stack, stop_event):
    while not stop_event.is_set():
        try:
            # 添加超时，避免永久阻塞
            item = await asyncio.wait_for(source_queue.get(), timeout=0.01)
            await dest_stack.put(item)
        except asyncio.TimeoutError:
            continue

async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)  # 初始延迟
    #print(1)
    for _ in range(count):
        item = await stack.get()
        print(item)
        await asyncio.sleep(delay)
    # 读取完成后发送停止信号

    stop_event.set()
    #print(stop_event.is_set())


async def main():
    # 读取输入参数
    input_str = input().strip()

    delay1, delay2, delay3, count = map(int, input_str.split(','))
    # 创建数据结构和同步机制

    queue1 = asyncio.Queue()  # 第一个writer的队列
    #stack = asyncio.LifoQueue()  # 栈（后进先出）
    stack = asyncio.Queue()
    stop_event = asyncio.Event()  # 停止事件

    # 创建并运行所有任务

    async with asyncio.TaskGroup() as tg:
        # 立即启动第一个writer
        wr1 = tg.create_task(writer(queue1, delay1, stop_event))

        # 等待一小段时间
        await asyncio.sleep(0.07)

        # 启动第二个writer
        wr2 = tg.create_task(writer(queue1, delay2, stop_event))

        # 其他任务
        tg.create_task(stacker(queue1, stack, stop_event))
        tg.create_task(reader(stack, count, delay3, stop_event))

asyncio.run(main())



