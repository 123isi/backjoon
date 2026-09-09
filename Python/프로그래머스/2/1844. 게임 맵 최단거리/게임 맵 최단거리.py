from collections import deque
def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    x=deque([(0,0)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while x:
        a,b=x.popleft()
        for i in range(4):
            a1=a+dx[i]
            b1=b+dy[i]
            if a1<0 or a1>=n or b1<0 or b1>=m:
                continue
            elif maps[a1][b1]==0:
                continue
            elif maps[a1][b1]==1:
                maps[a1][b1] = maps[a][b] + 1
                x.append((a1,b1))
                
    if maps[-1][-1] == 1: 
        return -1
        
                
    return maps[-1][-1]