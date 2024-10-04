x=int(input())
li=list(map(int,input().split()))
li.sort()
a=0
b=0
for i in range(x):
    a+=li[i]
    b+=a
print(b)
#1 3 6 9 13