import fractions
def eval_poly(coefficients, degree, x):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (x**(degree-i))
    return result
def universal_check(s, w, deg_A, coef_A, deg_B, coef_B):
    s = fractions.Fraction(s)
    w = fractions.Fraction(w)
    coef_A = [fractions.Fraction(str(c)) for c in coef_A]
    coef_B = [fractions.Fraction(str(c)) for c in coef_B]
    A = eval_poly(coef_A, deg_A, s)
    B = eval_poly(coef_B, deg_B, s)
    if B == 0:
        return False
    return A/B == w

def check():
    inp = [fractions.Fraction(x.strip()) for x in input().split(',')]
    #print(inp)
    s = inp[0]
    w = inp[1]
    deg_A = int(str(inp[2]))
    coef_A = inp[3:3+deg_A+1]
    index_deg_B = 4 + deg_A
    deg_B = int(inp[index_deg_B])
    coef_B = inp[index_deg_B+1:index_deg_B+1+deg_B+1]
    #print(eval_poly(coef_A, deg_A, s))
    #print(eval_poly(coef_B, deg_B, s))
    #print(f"s = {s}, w = {w}, deg_A = {deg_A}, coef_A = {coef_A} deg_B = {deg_B}, coef_B = {coef_B}")
    return universal_check(s, w, deg_A, coef_A, deg_B, coef_B)





if check():
    print("True")
else:
    print("False")