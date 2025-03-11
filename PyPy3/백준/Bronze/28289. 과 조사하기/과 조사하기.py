x=int(input())
a1=0
a2=0
a3=0
a4=0
for i in range(x):
    a,b,c=map(int,input().split())
    if a==1:
        a1+=1
    else:
        if b==1 or b==2:
            a2+=1
        elif b==3:
            a3+=1
        else:
            a4+=1
print(a2)
print(a3)
print(a4)
print(a1)