
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
arr = [1] * n
for i in range(n):
    for j in range(n):
        if i != j:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                arr[i] += 1
print(" ".join(map(str, arr)))
