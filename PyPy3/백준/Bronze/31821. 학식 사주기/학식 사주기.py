a=int(input())
li=[]
for i in range(a):
    li.append(int(input()))
b=int(input())
re=0
for i in range(b):
    a=int(input())
    re+=li[a-1]
print(re)