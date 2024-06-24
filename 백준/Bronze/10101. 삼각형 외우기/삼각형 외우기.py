x=int(input())
y=int(input())
z=int(input())
if x==y==z==60:
    print("Equilateral")
elif x+y+z!=180:
    print("Error")
elif x!=y and x!=z and y!=z:
    print("Scalene")
else:
    print("Isosceles")