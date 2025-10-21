def seqlen(seq):
    yield from seq
    return len(seq)
e = seqlen("EWT")
print(next(e))
print(next(e))
print(next(e))

def glue(*seq):
    for s in seq:
        length = yield from seqlen(s)
        yield length

print(list(glue("QWE",range(3))))
