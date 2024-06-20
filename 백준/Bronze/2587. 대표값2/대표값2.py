li=[]
for i in range(5):
    a=int(input())
    li.append(a)
b=0
for i in li:
   b+=i
li.sort()
print(f'{b/5:.0f}')
print(li[2])