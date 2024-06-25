x=int(input())
y=int(input())
z=int(input())
a=x*y*z
li= list(map(int, str(a)))

num1=0





num2=0

num3=0

num4=0

num5=0

num6=0

num7=0

num8=0

num9=0
num0=0



for i in li:
    if i==1:
        num1+=1
    elif i==2:
        num2+=1
    elif i==3:
        num3+=1
    elif i==4:
        num4+=1
    elif i==5:
        num5+=1
    elif i==6:
        num6+=1
    elif i==7:
        num7+=1
    elif i==8:
        num8+=1
    elif i==9:
        num9+=1
    else:
        num0+=1
print(num0)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)
