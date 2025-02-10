a=int(input())
arr=[]
for i in range(a):
    b=input()
    arr.append(b)
li=set(arr)
arr=list(li)
arr.sort(key=lambda x:(len(x),x))

for i in arr:
    print(i)