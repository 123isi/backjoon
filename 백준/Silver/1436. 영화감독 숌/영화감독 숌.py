x=int(input())
y = 0
result = 666
while True:
    if '666' in str(result):
        y+=1
    if y==x:
        break
    result+=1
print(result)