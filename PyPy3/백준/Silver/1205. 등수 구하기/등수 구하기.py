x, y, z = map(int, input().split())
if x != 0:
    li = list(map(int, input().split()))
else:
    li = []
li.append(y)
li.sort(reverse=True)
if x==z and y==li[-1]:
    print(-1)
    exit()
if len(li) > z:
    li.pop()

if li.count(y) > 1 and li.index(y) >= z:
    print(-1)
else:
    print(li.index(y) + 1)
