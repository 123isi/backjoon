li=[]
x=int(input())
for i in range(x):
    a=input()
    li.append(a)
li=list(set(li))
li.sort()
li.sort(key=len)

for i in li:
    print(i)