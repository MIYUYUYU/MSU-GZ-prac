a = list(range(5, 16))
b = [chr(c) for c in range(ord('a'), ord('k') + 1)]

a[3:6] = b[len(b)-5:len(b)]
print(a)
print(b)