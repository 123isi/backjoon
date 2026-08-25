a = int(input())
b = int(input())
li = []

for i in range(a, b+1):
    if i==2:
        li.append(i)
        continue
    elif i < 2:
        continue
    x = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            x = False
            break
    if x:
        li.append(i)
if len(li) == 0:
    print(-1)
    exit(0)
print(sum(li))
print(min(li))