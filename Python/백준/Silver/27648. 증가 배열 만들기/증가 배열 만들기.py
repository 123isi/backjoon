n,m,k=map(int,input().split())
if k<n+m-1:
    print("NO")
else:
    print("YES")
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(i+j+1)
        print(*row)
