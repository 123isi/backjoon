arr=[]
li=[]
for i in range(8):
    x=int(input())
    li.append(x)
    arr.append(x)
arr.sort()
an=[arr[-2],arr[-1],arr[-5],arr[-3],arr[-4]]
print(sum(an))
an1=[]
for i in an:
    an1.append(li.index(i))

an1.sort()
for i in an1:
    print(i+1,end=" ")