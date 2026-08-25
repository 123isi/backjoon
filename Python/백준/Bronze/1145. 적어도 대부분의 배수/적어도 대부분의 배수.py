import math

a,b,c,d,e=map(int,input().split())
li=[a,b,c,d,e]
ma=math.inf
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ma=min(ma,math.lcm(li[i],li[j],li[k]))
print(ma)