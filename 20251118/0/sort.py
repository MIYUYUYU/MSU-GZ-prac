import sys
with open(sys.argv[1], 'r+') as file:
    print(*sorted(file.readlines()), file = file)    
