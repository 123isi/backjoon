a = input().strip()
b = input().strip()

x = len(a)
arr = {}
for i, j in enumerate(a):
    arr[j] = i

y = len(b)

result = 0
for i in range(1, y):
    result = (result + pow(x, i, 900528)) % 900528
q = 0
for i in b:
    q = (q * x + arr[i]) % 900528

result = (result + q + 1) % 900528
print(result)
