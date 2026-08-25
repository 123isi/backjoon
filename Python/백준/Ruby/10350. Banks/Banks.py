n = int(input())
s = list(map(int, input().split()))
cnt = 0
total_sum = sum(s)

for i in range(n):
    tmp = 0
    for j in range(i, i + n):
        tmp += s[j % n]
        if tmp < 0:
            cnt += ((-tmp - 1) // total_sum) + 1

print(cnt)
