a,b=map(int,input().split())
for i in range(a):
    x,y=map(int,input().split())
f=0
for i in range(b):
    c,d=map(int,input().split())
    f+=d
print(f'{f/a:.4f}')
