a=int(input())
b=int(input())
c=b-a
if 1<c and c<=20:
    print("You are speeding and your fine is $",end="")
    print(100,end="")
    print(".")
elif c>=21 and c<=30:
    print("You are speeding and your fine is $",end="")
    print(270,end="")
    print(".")
elif c>=31:
    print("You are speeding and your fine is $",end="")
    print(500, end="")
    print(".")
else:
    print("Congratulations, you are within the speed limit!")