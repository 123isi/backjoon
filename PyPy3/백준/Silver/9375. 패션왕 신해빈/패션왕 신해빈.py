a = int(input())
for i in range(a):
    x = int(input())
    li = {}
    for j in range(x):
        b, c = input().split()
        li[c] = li.get(c, 0) + 1

    result = 1
    for v in li.values():
        result *= (v + 1)
    print(result - 1)
