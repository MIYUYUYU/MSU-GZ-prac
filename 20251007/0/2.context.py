from decimal import Decimal
from decimal import getcontext
a = Decimal("44.44")
print(a.sqrt())
print(getcontext())
getcontext().prec = 50
print(a.sqrt())