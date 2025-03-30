import math

a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr = arr + [0, 0, 0, 0]

s = 0
e = 0
su = arr[0]
how = 1
r = math.inf

while True:
    if su >= b:
        r = min(r, how)
        su -= arr[s]
        s += 1
        how -= 1
    elif e + 1 < a:
        e += 1
        su += arr[e]
        how += 1
    else:
        break

if r == math.inf:
    print(0)
else:
    print(r)
