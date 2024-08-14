x, y = map(int, input().split())
result = []

for i in range(x, y+1):
    p = True
    if i < 2:
        p = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            p = False
            break
    if p:
        result.append(i)

for num in result:
    print(num)
