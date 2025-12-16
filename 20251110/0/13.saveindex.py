def itemget(collection, index):
    return collection[index]

def safesafeindex(function, *args):
    try:
        try:
            return function(*args)
        except Exception as e:
            raise IndexError from e
    except IndexError as ie:
        if isinstance(ie.__cause__, IndexError):
            return None
        return f'NotANone: {ie.__cause__}'

print(list(safesafeindex(itemget,"qwe",i) for i in range(5)))
print(safesafeindex(eval,'1/0'))