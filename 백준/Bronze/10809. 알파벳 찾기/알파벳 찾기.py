x=input()
a=list(x)
d=0
arr=[-1 for i in range(26)]
for i in a:
    b=ord(i)
    c=b-97
    if arr[c]==-1:
        arr[c]=d
    d+=1

for i in range(26):
    print(arr[i],end=' ')
