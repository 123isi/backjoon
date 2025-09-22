a=int(input())
r=0
for i in range(a):
    x,y=input().split("-")
    if int(y)<=90:
        r+=1
print(r)