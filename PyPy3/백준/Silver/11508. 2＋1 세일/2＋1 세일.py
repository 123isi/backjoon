n = int(input())
li= []
arr = []
result = 0

for _ in range(n):
  li.append(int(input()))
li.sort(reverse=True)

for i in range(0, len(li), 3):
  arr.append(li[i : i + 3])

for i in arr:
  if len(i)>2:
    result += sum(i) - min(i)
  else:
    result += sum(i)

print(result)