a = int(input())
arr = list(map(int, input().split()))
li1 = [(val, idx) for idx, val in enumerate(arr)]
li1.sort()
result = [0] * a
for rank, (val, idx) in enumerate(li1):
    result[idx] = rank
print(*result)
