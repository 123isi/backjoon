x=int(input())
for i in range(x):
    li=list(map(int,input().split()))
    li.sort()
    print(li[-3])