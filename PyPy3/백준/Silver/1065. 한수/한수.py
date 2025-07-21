a=int(input())
cnt=0
for i in range(1,a+1):
    if i<100:
        cnt+=1
    else:
        if (i%100)//10==i%10 and i%10==i//100:
            cnt+=1
        elif (i%100)//10-i%10==i//100-(i%100)//10:
            cnt+=1
print(cnt)