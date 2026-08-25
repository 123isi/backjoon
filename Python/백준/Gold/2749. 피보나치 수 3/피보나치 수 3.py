x = int(input())
f = [0, 1]
y = 1000000//10*15
for i in range(2,y):
    f.append(f[i-1]+f[i-2])
    f[i] %= 1000000
print(f[x%y])