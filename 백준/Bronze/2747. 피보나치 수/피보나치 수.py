x=int(input())
a=0
b=1
s=0
while True:
    c=a
    a=b
    b=c+a
    s+=1
    if s>=x:
        break
print(a)