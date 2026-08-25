a=int(input())
for i in range(a):
    x,y,z,b,c=map(int,input().split())
    print(f'Case #{i+1}: {max(x,y,z,b,c)}')