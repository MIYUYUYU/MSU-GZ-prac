while True:
    inp = input()
    try:
        int(inp)

    except ValueError:
        print("enter a number")

    else:
        print("OK")
        break
