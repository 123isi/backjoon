x=int(input())
arr=[0,0,1,0,1,1]
for i in range(6,x+1):
        if arr[i-1]+arr[i-3] + arr[i-4] == 3:
            arr.append(0)
        else:
            arr.append(1)

if arr[x] == 0:
    print("CY")
else:
    print("SK")
