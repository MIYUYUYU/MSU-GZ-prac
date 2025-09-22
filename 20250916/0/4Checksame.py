num = 0
sum = 0
while (x := int(input())) != 0:
    num += 1
    if x == num:
        sum += 1
print(sum)