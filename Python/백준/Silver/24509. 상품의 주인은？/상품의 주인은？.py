a = int(input())
li = {}

for i in range(a):
    a, b, c, d, e = map(int, input().split())
    li[a] = (b, c, d, e)
arr=[]

for i,j in sorted(li.items(), key=lambda x: (-x[1][0],x[0])):
    if i not in arr:
        print(i,end=" ")
        arr.append(i)
        break
for i,j in sorted(li.items(), key=lambda x: (-x[1][1],x[0])):
    if i not in arr:
        print(i, end=" ")
        arr.append(i)
        break
for i,j in sorted(li.items(), key=lambda x: (-x[1][2],x[0])):
    if i not in arr:
        print(i, end=" ")
        arr.append(i)
        break
for i,j in sorted(li.items(), key=lambda x: (-x[1][3],x[0])):
    if i not in arr:
        print(i, end=" ")
        arr.append(i)
        break