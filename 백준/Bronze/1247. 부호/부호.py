a=0
for i in range(0,3):
    x=int(input())
    for j in range(x):
        y=int(input())
        a+=y
    if a==0:
        print(0)
    elif a<0:
        print("-")
    else:
        print("+")
    a=0