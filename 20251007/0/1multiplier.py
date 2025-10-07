import decimal
import fractions

def multiplier(x, y, Type):
    # if Type == "decimal":
    #     return decimal.Decimal(x) * decimal.Decimal(y)
    # elif Type == "float":
    #     return float(x) * float(y)
    # elif Type == Fraction:
    #     return fractions.Fraction(x) * fractions.Fraction(y)
        return Type(x) * Type(y)
for t in (float, decimal.Decimal, fractions.Fraction):
    print(multiplier("1.3","5.7",t))