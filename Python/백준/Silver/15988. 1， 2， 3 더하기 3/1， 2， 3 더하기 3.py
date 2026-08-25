a = int(input())
for i in range(a):
    b = int(input())
    if b == 1:
        print(1)
        continue
    elif b == 2:
        print(2)
        continue
    elif b == 3:
        print(4)
        continue

    k, l, m = 1, 2, 4
    for j in range(4, b + 1):
        t = (k + l + m)%1000000009
        k = l
        l = m
        m = t
    print(m)
