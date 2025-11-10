def div(a, b, eps):
    if abs(b) < abs(eps):
        raise ZeroDivisionError
    return a / b
