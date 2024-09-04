def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
x = int(input())
a = factorial(x)
a_str = str(a)
b = 0
c = len(a_str)
while c > 0:
    if a_str[c-1] == '0':
        b += 1
        c -= 1
    else:
        break
print(b)
