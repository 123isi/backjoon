x = int(input())
li = None

for _ in range(x):
    row = list(map(int, input().split()))
    if li is None:
        li = sorted(row, reverse=True)[:x]
    else:
        li.extend(row)
        li.sort(reverse=True)
        li = li[:x]

print(li[x-1])
