x,y=map(int,input().split())
li=[]
for i in range(1,x+1):
    if x%i==0:
        li.append(i)
li.sort()
if len(li)<y:
    print(0)
else:
    print(li[y-1])