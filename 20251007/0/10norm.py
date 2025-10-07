
def bih(a, b):
    bw, hw = len(bin(b)), len(hex(b))
    for i in range(a, b + 1):
        print(f"{i:<#{bw}b} = {i:#{hw}x}")
print(bih(12,35))