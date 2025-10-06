def pareto(*T):
    n = len(T)
    result = []

    for i in range(n):
        find = False
        for j in range(n):
            if i == j:
                continue
            if T[i][0] <= T[j][0] and T[i][1] <= T[j][1] and (T[i][0] < T[j][0] or T[i][1] < T[j][1]):
                find = True
                break
            else:
                continue
        if find:
            continue
        else:
            result.append(T[i])

    return tuple(result)

inp = eval(input())
print(pareto(*inp))