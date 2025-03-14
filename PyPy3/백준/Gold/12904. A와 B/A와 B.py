a = input()
b = input()

while len(b) > len(a):
    if b[-1] == "A":
        b = b[:-1]
    elif b[-1] == "B":
        b = b[:-1][::-1]

if a==b:
    print(1)
else:
    print(0)
