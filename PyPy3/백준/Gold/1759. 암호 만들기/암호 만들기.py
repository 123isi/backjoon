from itertools import combinations

a,b=map(int,input().split())
li=list(input().split())
li.sort()
vowels={'a','e','i','o','u'}

for i in combinations(li,a):
    cnt=0
    for j in i:
        if j in vowels:
            cnt+=1
    if cnt>=1 and a-cnt>=2:
        for j in i:
            print(j,end='')
        print()
