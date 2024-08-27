x=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
a=0
for i in range(1,x):
    a+=li[0]+li[i]
print(a)