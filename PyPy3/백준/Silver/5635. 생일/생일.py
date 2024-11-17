a = int(input())
arr = []

for i in range(a):
    li = list(input().split())
    li[2]=int(li[2])
    li[3]=int(li[3])
    li[1]=int(li[1])
    arr.append(li)

arr.sort(key=lambda x: (x[3], x[2], x[1]))
print(arr[-1][0])
print(arr[0][0])
