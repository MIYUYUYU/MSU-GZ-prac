if (N := int(input())) <= 0:
    print("Вводите целое положительное число")
else:
    L = M = N
    while N <= L + 2:
        M = L
        while M <= L + 2:
            mul = M * N
            sum_n = 0
            while mul // 1 != 0:
                sum_n += mul % 10
                mul //= 10
                #print(sum_n)
            if sum_n == 6:
                print(f"{N} * {M} = :=)",end=' ')
            else:
                print(f"{N} * {M} = {N * M}",end=' ')
            M += 1
        N += 1
        print()


