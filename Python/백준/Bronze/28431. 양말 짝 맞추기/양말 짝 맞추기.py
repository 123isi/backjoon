a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
li=[a,b,c,d,e]
arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in li:
    arr[i]+=1

for i in range(10):
    if arr[i]%2==1:
        print(i)