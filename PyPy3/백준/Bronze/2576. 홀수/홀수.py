li=[]
for i in range(7):
    a=int(input())
    li.append(a)
ar=[]
for i in li:
    if i%2==1:
        ar.append(i)
b=0
if len(ar)==0:
    print(-1)
else:

    for i in ar:
        b+=i
    print(b)
    print(min(ar))