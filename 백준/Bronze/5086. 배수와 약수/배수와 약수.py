x,y=map(int,input().split())
while x!=0 and y!=0:

    if y%x==0:
        print("factor")
    elif x%y==0:
        print("multiple")
    else:
        print("neither")
    x, y = map(int, input().split())