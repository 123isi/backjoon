import sys
input=sys.stdin.readline
a = int(input())

for i in range(a):
    b = int(input())
    if b == 1:
        print(1)
        continue
    c = 1
    a = False
    while c <= b:
        if c == b:
            a = True
            break
        c *= 2
    if a:
        print(1)
    else:
        print(0)
