a = [int(x) for x in input().split()]
print(a)
fl = True
for x in a:
    if x == 13:
        print("find 13")
        fl = False
        break
if fl:
    print("Not find 13")