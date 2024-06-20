li=[]
arr=[]
for i in range(10):
    a=int(input())
    li.append(a)
for i in range(10):
    a=int(input())
    arr.append(a)
li.sort()
arr.sort()
print(li[-1]+li[-2]+li[-3])
print(arr[-1]+arr[-2]+arr[-3])