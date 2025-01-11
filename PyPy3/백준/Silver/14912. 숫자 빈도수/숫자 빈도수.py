a,b=map(int,input().split())
li=[]
b=str(b)
re=0
for i in range(1,a+1):
    li=str(i)
    re+=li.count(b)
print(re)