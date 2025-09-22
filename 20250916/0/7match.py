match (int(input())):
    case 1:
        print("Один")
    case 2:
        print("Два")
    case 3:
        print("Три")
    case var if var % 2 == 0:
            print(var, "is Четный")
    case n:
        print(n,"много")