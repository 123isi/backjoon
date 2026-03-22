li=[]

for i in range(9):
    x=int(input())
    li.append(x)
li.sort()
sum1=sum(li)

for k in range(9):
    for w in range(k+1,9):
        if sum1-li[k]-li[w]==100:
            li.remove(li[k])
            li.remove(li[w-1])
            break
    if len(li)==7:
        break
for i in li:
    print(i)