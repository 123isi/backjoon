num = int(input())
a = 1
cnt = 1
while num > a:
    a += 6 * cnt
    cnt += 1
print(cnt)