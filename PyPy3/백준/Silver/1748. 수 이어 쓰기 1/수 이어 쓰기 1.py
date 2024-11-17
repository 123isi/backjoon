x = int(input())

max = 0  
re = 1   
a = 1   

while a <= x:
    b = min(x, a * 10 - 1) 
    max += (b - a + 1) * re 
    a *= 10  
    re += 1

print(max)
