from decimal import Decimal, getcontext

getcontext().prec = 50

e = Decimal("2.7182818284590452353602875")

n = int(input())

if n == 0:
    print(3)
else:
    print(round(e, n))
