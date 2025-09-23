# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j, end = " ")
#     print()
a = eval(input())
for a1 in a:
    if a1 % 2 != 0:
        print(a1)
        break
else:
    print(a[0])