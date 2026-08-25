a = int(input())
arr = list(map(int, input().split()))

li1 = [(val, idx) for idx, val in enumerate(arr)]
li1.sort()

result = [0] * a
rank = -1
prev_val = None

for val, idx in li1:
    if val != prev_val:
        rank += 1
    result[idx] = rank
    prev_val = val

print(*result)
