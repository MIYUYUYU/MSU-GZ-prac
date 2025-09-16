a = eval(input())

i, j = 0, 0
tmp = a[0]
while i < 3:
    j = i + 1
    while j < 3:
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        j += 1
    i += 1

print(a[0],a[1],a[2],sep=', ')


#enter
import sys
exec(sys.stdin.read())

