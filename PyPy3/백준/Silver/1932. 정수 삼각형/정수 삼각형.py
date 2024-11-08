a = int(input())
arr = []

for i in range(a):
    li = list(map(int, input().split()))
    arr.append(li)

for i in range(1, a):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i]) - 1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

ma = max(arr[-1])
print(ma)
