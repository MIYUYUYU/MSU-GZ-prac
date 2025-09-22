sum = 0
while (inp:= int(input())) > 0:
    sum += inp
    if sum > 21:
        print(sum)
        break
else:
    print(inp)
