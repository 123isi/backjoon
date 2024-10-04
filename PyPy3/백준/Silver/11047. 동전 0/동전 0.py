import sys
input=sys.stdin.readline
b=0
result=0
li=[]
x,y=map(int,input().split())
for i in range(x):
    a=int(input())
    li.append(a)
li.sort(reverse=True)
while y>0:
    if y>=li[b] and b<len(li):
        y-=li[b]
        result+=1
    else:
        b+=1
print(result)