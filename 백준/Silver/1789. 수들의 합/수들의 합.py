x=int(input())
a=0
for i in range(4294967295):
    if a>x:
        break
    a=a+i
print(i-2)