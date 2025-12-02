def meet(n):
    for i in range(n):
        yield f'{i}: Hello'

    return f'You {3}: Bye!'

def meeting(m):
    for i in range(m):
        res = yield from meet(3)
        yield f'<{i}>: {res}'
    return 'FIN'
i = meeting(2)

try:
    while True:
        print(next(i))
except StopIteration as E:
    print(E.value)

def meet(n):
    for i in range(n):
        yield f'{i}: Hello'

    return f'You {n}: Bye!'

