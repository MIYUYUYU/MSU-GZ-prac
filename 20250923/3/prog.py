arr1 = []
arr2 = []
line = [int(x.strip()) for x in input().split(',')]
if len(line) == 1:
    arr1.append(line[0])
    arr2.append(int(input()))
    mul = arr1[0] * arr2[0]
    print(mul)
    exit(0)
arr1.append(line)
for i in range(1,len(line)):
    line = list(eval(input()))
    #print(line)
    arr1.append(line)
for i in range(len(line)):
    line = list(eval(input()))
    arr2.append(line)

mul = []

for i in range(len(line)):
    mul_line = []
    for j in range(len(line)):
        sum = 0
        for k in range(len(line)):
            sum += arr1[i][k] * arr2[k][j]
        mul_line.append(sum)
    mul.append(mul_line)
for line in mul:
    print(*line, sep=', ')
# while (line := eval(input()) and len(arr1)) < len(line):
#     arr1.append(line)
# while (line := eval(input()) and len(arr2)) < len(line):
#     arr2.append(line)

# print(arr1)
# print()
# print(arr2)