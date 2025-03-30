import math
n=int(input())
if n==1:
    print(0)
else:
    cnt=0
    tmp=n
    for i in range(2,int(math.sqrt(n))+1):
        while tmp%i==0:
            cnt+=1
            tmp//=i
    if tmp>1:
        cnt+=1
    c=cnt
    print(math.ceil(math.log2(c)))
