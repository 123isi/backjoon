x=int(input())
y=list(map(int,input().split()))
a=0
b=0
for i in y:
    if i%2==0:
        a+=1
    else:
        b+=1
if b<a:
    print("Happy")
else:
    print("Sad")