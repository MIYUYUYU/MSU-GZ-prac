inp = input()
inp = inp.lower()
#print(inp)
pairs = set()
for i in range(len(inp) - 1):
    if inp[i].isalpha() and inp[i + 1].isalpha():
        pairs.add(inp[i]+inp[i+1])

print(len(pairs))