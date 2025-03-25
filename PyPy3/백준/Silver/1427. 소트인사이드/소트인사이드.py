a=input()
li=list(str(a))
arr=[]
for i in li:
    arr.append(int(i))
li.sort(reverse=True)
for i in li:
    print(i,end="")