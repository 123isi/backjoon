a, b = map(int, input().split())
li = {}
for i in range(a):
    c = input().strip()
    li[c] = i + 1
reverse_li = {v: k for k, v in li.items()}

for i in range(b):
    c = input().strip()
    if c in li:
        print(li[c])
    else:
        if c.isdigit():
            idx = int(c)
            if idx in reverse_li:
                print(reverse_li[idx])
