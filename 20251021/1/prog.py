def fib(m, n):
    a = 1
    b = 1
    index = 0
    out_count = 0
    output = []
    if m == 0:
        yield a
        out_count += 1
    while True:
        tmp = a + b
        a = b
        b = tmp
        index += 1
        #print(index)
        if index >= m and out_count < n:

            output.append(a)
            #print(f"a = {a}, index = {index}")
            out_count += 1

            #print(out_count)
            yield a
        elif index < m and out_count < n:
            #print(f"a = {a}, index = {index}")
            continue
        else:
            break

    #yield output


eval(input())