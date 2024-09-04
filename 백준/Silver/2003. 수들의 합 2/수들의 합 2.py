
N, M = map(int, input().split())
A = list(map(int, input().split()))
count = 0
li = 0
start = 0
for end in range(N):
    li += A[end]
    while li > M:
        li -= A[start]
        start += 1
    if li == M:
        count += 1

print(count)
