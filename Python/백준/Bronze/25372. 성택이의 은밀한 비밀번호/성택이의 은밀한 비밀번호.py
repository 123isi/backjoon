a=int(input())
b=[]
for i in range(a):
    b=input()
    b=list(b)
    if len(b)>=6 and len(b)<=9:
        print("yes")
    else:
        print("no")
    b=[]