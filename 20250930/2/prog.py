def sub(a,b):
    if isinstance(a,(int,float,complex)):
        return a-b
    elif isinstance(a,(list,tuple)):
        result = []
        for item in a:
            if item in b:
                continue
            else:
                result.append(item)
        if isinstance(a,tuple):
            return tuple(result)
        else:
            return result

inp = eval(input())
print(sub(inp[0],inp[1]))

