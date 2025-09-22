a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
li=[a,b,c,d,e,f]
count=li.count("W")
if count==5 or count==6:
    print(1)
elif count==4 or count==3:
    print(2)
elif count==2 or count==1:
    print(3)
else:
    print(-1)