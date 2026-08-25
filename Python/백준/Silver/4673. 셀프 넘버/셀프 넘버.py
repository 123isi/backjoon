def selfnum(a):
    re = a
    while a > 0:
        re += a % 10
        a //= 10
    return re
self1 = set(range(1, 10001))
arr=set()
for i in range(1,10001):
    if selfnum(i) <=10000:
        arr.add(selfnum(i))
self1-=arr
self2=list(self1)
self2.sort()
for i in self2:
    if i>10000:
        exit()
    print(i)