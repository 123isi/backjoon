li=[]
for i in range(10):
    a=int(input())
    li.append(a%42)
li.sort()
a=set(li)
print(len(a))