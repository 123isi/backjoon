x = int(input())  
y = int(input())  
li = [int(input()) for _ in range(x-1)] 

a = 0  


while True:
    li.sort(reverse=True)  
    if x == 1 or y > li[0]:
        break
    li[0] -= 1  
    y += 1  
    a += 1

print(a)