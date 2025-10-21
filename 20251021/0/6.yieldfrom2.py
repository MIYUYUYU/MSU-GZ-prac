def travel(n):
    yield from ["по кочкам"] * n
    return "и в яму"

def travelwrap(n):
    yield (yield from travel(n))

print(*travelwrap(4),sep='\n')