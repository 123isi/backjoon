a=int(input())
b=2024
c=8
for i in range(a-1):
    c+=7
    if c>12:
        c-=12
        b+=1
print(b,c)