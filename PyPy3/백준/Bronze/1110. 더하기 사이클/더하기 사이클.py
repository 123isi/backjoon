a = int(input())
b = a
c = 0
while True:
    x = a // 10
    y = a % 10
    z = x + y
    a = (y * 10) + (z % 10)
    c += 1
    if a == b:
        break
print(c)
