import re
b=0
a = input()
arr=list(a)

li = re.findall(r'pi|ka|chu', a)
for i in li:
    if i=='pi' or i=='ka':
        b+=2
    elif i=='chu':
        b+=3
if b==len(arr):
    print('YES')
else:
    print('NO')