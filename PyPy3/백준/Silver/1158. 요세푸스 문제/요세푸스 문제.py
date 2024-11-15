x, y = map(int, input().split())
li = []
li1 = []
a = 0
for i in range(x):
    li.append(i)

while li:
    a = (a + y - 1) % len(li)
    li1.append(li[a])
    li.pop(a)
print("<",end="")
b=0
for i in li1:
    b+=1
    print(i+1,end="")
    if b<len(li1):
        print(", ",end="")
print(">")