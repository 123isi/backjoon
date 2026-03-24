li=[]
for i in range(10):
    li.append(int(input()))
li.append(0)
j=0
re=0
while 1:
    re+=li[j]
    if re==100:
        break
    if re>100:
        if re-100==100-re+li[j]:
            break
        elif re-100<100-re+li[j]:
            break
        elif re-100>100-re+li[j]:
            re=re-li[j]
            break
    if j==9:
        break
    j+=1
print(re)