x=int(input())
if x%100==10:

    a=x%100
    b=x//100
    print(a+b)
else:
    a=x%10
    b=x//10
    print(a+b)