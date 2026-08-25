x=int(input())
for i in range(2,x+1):
    if x%i==0:
        while 1:
            if x%i!=0:
                break
            print(i)
            x=x//i
