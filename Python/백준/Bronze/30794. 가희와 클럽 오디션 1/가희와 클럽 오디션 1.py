a,b=input().split()
c=int(a)
if b=="miss":
    print(0)

elif b=="bad":
    print(c*200)
elif b=="cool":
    print(c*400)
elif b=="great":
    print(c*600)
else:
    print(c*1000)