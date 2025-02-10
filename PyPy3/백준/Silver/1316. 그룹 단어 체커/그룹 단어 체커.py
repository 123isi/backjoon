a=int(input())
arr=[]
cnt=0
t=0
for i in range(a):
    b=input()
    li=list(b)
    arr = [li[0]]
    for j in range(1,len(li)):
        if li[j] in arr and li[j]!=arr[-1]:
            cnt-=1
            break
        arr.append(li[j])
    cnt+=1
print(cnt)