a = input().strip()
li = list(a)

cnt = 10
now = li[0]

for i in range(1, len(li)):
    if now == li[i]:
        cnt += 5
    else:
        cnt += 10
    now = li[i]

print(cnt)
