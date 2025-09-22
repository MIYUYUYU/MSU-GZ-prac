inp = int(input())
if inp % 2 == 0 and inp % 25 == 0:
    print("A +",end=' ')
else:
    print("A -",end=' ')
if inp % 2 != 0 and inp % 25 == 0:
    print("B +",end=' ')
else:
    print("B -",end=' ')
if inp % 8 == 0:
    print("C +",end=' ')
else:
    print("C -",end=' ')