a,b,c,d,e=map(int,input().split())
if 4*e-a-b-c-d<0:
    print(0)
    exit()
print(4*e-a-b-c-d)