x = int(input())
li = list(map(int, input().split()))
y = int(input())

start = 0
end = max(li)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in li:
        total += min(i, mid)
    if total <= y:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
