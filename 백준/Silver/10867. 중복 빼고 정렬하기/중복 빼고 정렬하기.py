x=int(input())
li=list(map(int,input().split()))
li.sort()
a=set(li)
for i in a:
    print(i,end=' ')
