import itertools
a, b = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
arr=[]
for i in itertools.combinations(li, b):
    arr.append(i)
arr=set(arr)
arr=list(arr)
arr.sort()
for i in arr:
    print(*i)