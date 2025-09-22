ar="N"
for i in range(10):
    a=int(input())
    if a==1:
        if ar=="N":
            ar="E"
        elif ar=="E":
            ar="S"
        elif ar=="S":
            ar="W"
        elif ar=="W":
            ar="N"
    elif a==2:
        if ar=="N":
            ar="S"
        elif ar=="S":
            ar="N"
        elif ar=="E":
            ar="W"
        elif ar=="W":
            ar="E"
    else:
        if ar=="N":
            ar="W"
        elif ar=="E":
            ar="N"
        elif ar=="S":
            ar="E"
        elif ar=="W":
            ar="S"
print(ar)