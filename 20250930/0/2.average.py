def average(a, *args):
    return sum([a, *args])/(len(args)+1)

print(average(2,3,4,9))