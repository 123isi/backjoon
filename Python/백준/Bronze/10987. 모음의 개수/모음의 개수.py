a=input()
li=list(a)
sum=0
for i in li:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        sum+=1
print(sum)