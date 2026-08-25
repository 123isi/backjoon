x=int(input())
li=[]
for i in range(x):
    li.append(int(input()))
li.sort()
a=f'{sum(li)/x:.0f}'
if a=='-0':
    print(0)
else:
    print(a)
print(li[x//2])
arr = [0] * 8001
for i in li:
    arr[i+4000]+=1
li1=list(enumerate(arr))
li2 = sorted(li1, key=lambda x: x[1], reverse=True)
if li2[0][1]==li2[1][1]:
    print(li2[1][0]-4000)
else:
    print(li2[0][0]-4000)
print(max(li)-min(li))