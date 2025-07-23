a=input()
li=list(a)
arr=[0]*26
for i in range(len(li)):
    if ord(li[i])>=97:
        arr[ord(li[i])-97]+=1
    else:
        arr[ord(li[i])-65]+=1
max1=0
r=""
for i in range(len(arr)):
    if arr[i]>max1:
        max1=arr[i]
        r=chr(i+65)
    elif max1==arr[i]:
        r="?"
print(r)