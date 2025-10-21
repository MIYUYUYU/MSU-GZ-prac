def pargen():
    var = yield "START"
    while var:
        var = yield f"{var}"
    yield "END"
g = pargen()
print(next(g))

print(g.send(123))
g.send(1)
print(next(g))