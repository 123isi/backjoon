from decimal import Decimal, getcontext
getcontext().prec = 2000
a, b = input().split()
result = Decimal(a) ** int(b)
print(format(result, 'f').rstrip('0').rstrip('.'))
