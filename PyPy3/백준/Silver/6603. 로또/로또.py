from itertools import combinations

a=[1]
while 1:
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    check=a[1:]
    for i in combinations(check,6):
        print(*i)
    print()