def fib(n, cn):
    if n == 1 or n == 2:
        return 1
    else:
        cn += 1
        return fib(n - 1, cn) + fib(n - 2, cn)

def fibonacci(n, dn):
    f = [0] * n
    if n > 0:
        f[0] = 0
    if n > 1:
        f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        dn += 1
    return dn

a = int(input())
cn = 0
dn = 0
c = fib(a, cn)
d = fibonacci(a, dn)
print(c, d)
