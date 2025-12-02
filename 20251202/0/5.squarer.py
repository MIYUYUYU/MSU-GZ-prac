import asyncio
async def squarer(n):
    return n**2

async def doubler(n):
    return 2 * n

async def main(x, y):
    x, y = await asyncio.gather(squarer(x), squarer(y))
    x, y = await asyncio.gather(doubler(x), doubler(y))
    print([x, y])

asyncio.run(main(*eval(input())))