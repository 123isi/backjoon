a = int(input())
b = int(input())

ans = b  

if a >= 5:
    ans = min(ans, b - 500)
if a >= 10:
    ans = min(ans, b - b // 10)  
if a >= 15:
    ans = min(ans, b - 2000)
if a >= 20:
    ans = min(ans, b - b // 4)  

if ans < 0:
    ans = 0

print(ans)
