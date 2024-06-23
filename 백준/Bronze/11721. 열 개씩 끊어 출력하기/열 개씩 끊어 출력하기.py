a=input()
b=1
li=list(a)
for i in range(0,len(li)):
    if i==0:
        b+=1
    elif i%10==0:
        print()
    print(li[i],end='')