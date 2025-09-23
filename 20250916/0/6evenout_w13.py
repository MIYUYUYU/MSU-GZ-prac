fl = False
while x := int(input()):
    if x == 13:
        fl = True
        print("find 13 :(")
        break
    elif x % 2 == 0:
        print(x)
if not fl:
    print("GOOD")
