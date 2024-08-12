x=int(input())
arr=[1,1,0,1,1]
for i in range(5,x+1):   
        if arr[i-1]+arr[i-3] + arr[i-4] == 3:
            arr.append(0)
        else:
            arr.append(1)

if arr[x] == 1:
    print("SK")
else:
    print("CY")