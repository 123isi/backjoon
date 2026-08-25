a = int(input())  
li = []
for _ in range(a):
    x, y = map(int, input().split())
    li.append((x, y))
li.sort(key=lambda arr: (arr[1], arr[0]))
b = 0
x = 0
for y, a in li:
    if y >= x:
        b += 1
        x = a
print(b)
