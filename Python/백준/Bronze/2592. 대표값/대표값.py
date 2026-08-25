from collections import Counter

li=[]
for i in range(10):
    li.append(int(input()))
print(sum(li)//10)
ct=Counter(li)
x=ct.most_common(1)
print(x[0][0])