x, y = map(int, input().split())
c = 1

while y > x:
    if y % 10 == 1:
        y //= 10
    elif y % 2 == 0:
        y //= 2
    else:
        break
    c += 1
if x==y:
    print(c)
    exit()
print(-1)

