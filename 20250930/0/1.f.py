print(*"FASDFA")
print(*range(1,20,2),sep=":")
def fnu(*args):
    for i in args:
        print(i)

fnu()
fnu(1,2,3,4)
fnu(*"EWR")