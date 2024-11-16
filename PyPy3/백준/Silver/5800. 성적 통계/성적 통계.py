x = int(input())
for i in range(x):
    li = list(map(int, input().split()))
    a = li[0]
    li = li[1:]
    li.sort(reverse=True)
    best = 0
    for j in range(1, len(li)):
        best = max(best, li[j - 1] - li[j])

    print(f"Class {i + 1}")
    print(f"Max {max(li)}, Min {min(li)}, Largest gap {best}")
