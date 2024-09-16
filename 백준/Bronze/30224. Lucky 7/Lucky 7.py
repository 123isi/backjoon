x=int(input())
y=str(x)
if '7' in y:
    if x%7==0:
        print(3)
    else:
        print(2)
else:
    if x%7==0:
        print(1)
    else:
        print(0)