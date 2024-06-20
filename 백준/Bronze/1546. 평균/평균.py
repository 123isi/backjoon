x = int(input()) 
y = list(map(int, input().split())) 
a = max(y)
b = [(score / a) * 100 for score in y]
c = sum(b) / x
print(c)
