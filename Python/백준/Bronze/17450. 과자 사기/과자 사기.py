res, ans = 0, 0
li = ["S", "N", "U"]
for i in range(3):
    cost, weight = map(int, input().split())
    c, w = cost * 10, weight * 10
    m = c - 500 if c >= 5000 else c
    if (w / m) > res:
        res = w / m
        ans = i
print(li[ans])