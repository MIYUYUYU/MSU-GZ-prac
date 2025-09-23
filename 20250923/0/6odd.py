from math import sin

# lst = [i * 2 + 1 for i in range(10) if i != 6]
# lst2 = [i*10+j for i in range(5) for j in range(5)]
# lst3 = [[0] * 4] * 3
# lst3[0][1] = "QQ"
# lst4= [[0]*4 for i in range(3)]
# lst4[0][0] = 'a'
# print(lst4)
range(11,28)
lst = [d for d in range(11,28) if d % 2 == 1 and '3' not in str(d)]
print(lst)