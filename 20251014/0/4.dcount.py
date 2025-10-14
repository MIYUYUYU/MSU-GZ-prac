c = {}
for w in input().split():
    c[w] = c.setdefault(w, 0) + 1
print(c)