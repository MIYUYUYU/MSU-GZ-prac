arr = []
while x := input():
    arr.append(list(eval(x)))

#print(arr[1][0])
for i in range(len(arr[0])):
    for j in range(i,len(arr[0])):
        arr[i][j], arr[j][i] = arr [j][i], arr[i][j]
        #print(arr[j][i],end=" ")
for line in arr:
    print(*line, sep = ', ')