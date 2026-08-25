a=int(input())
li=list()
for i in range(a):
    li.append(input())
arr=li.copy()
aa=li.copy()
aa.sort()
arr.sort(reverse=True)

if arr==li:
    print("DECREASING")
elif aa==li:
    print("INCREASING")
else:
    print("NEITHER")
