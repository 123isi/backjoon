x=int(input())
c=0
n=0
for i in range(x):
    a=int(input())
    if a==0:
        n+=1
    elif a==1:
        c+=1
if n>c:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")