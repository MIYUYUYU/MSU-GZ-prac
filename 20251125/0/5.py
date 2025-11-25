w1, w2, w3 = input().split()

while True:
    s = input().strip()
    if s == '': break
    words = s.split()
    match words:
        case [first, *rest] if first == w1 and "yes" in words:
            print("Case 1")
        case [single] if single == w2:
            print("Case 2")
        case [start, *middle, end] if start == w3 and end == w2:
            print("Case 3")
        case _:
            print("No match")