a, b, c = map(int, input().split())

x=max(b,a-b)
y=max(c,a-c)
z=x*y
print(z*4)