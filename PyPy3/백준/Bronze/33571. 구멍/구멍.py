a=input()
cnt=0
li=list(a)
for i in li:
    if i=="B":
        cnt+=2
    elif i=="@" or i=="A" or i=="d" or i=="D" or i=="a"  or i=="b" or i=="d" or i=="e" or i=="g" or i=="O" or i=="o" or i=="P" or i=="p" or i=="q" or i=="Q" or i=="R":
        cnt+=1
print(cnt)