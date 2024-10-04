li=list(input()) 
b=0  
while len(li) > 1:  
    a = 0
    for i in li:
        a+=int(i) 
    li=list(str(a)) 
    b+=1  
print(b)  
if int(li[0]) % 3 == 0: 
    print("YES")
else:
    print("NO")
