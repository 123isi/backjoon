x, y = map(int, input().split())
li1 =[]
li2 = set()
for i in range(x):
    a = input()
    li1.append(a)
for i in range(y):
    a = input()
    li2.add(a)
li = [i for i in li1 if i in li2]
print(len(li))
li.sort()
for i in li:
    print(i)