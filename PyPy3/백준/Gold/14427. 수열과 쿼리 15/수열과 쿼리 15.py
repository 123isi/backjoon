import sys
input = sys.stdin.readline

a = int(input())
li = list(map(int, input().split()))
b = int(input())
tree = [(float('inf'), float('inf'))] * (2 * a)

for i in range(a):
    tree[a + i] = (li[i], i)
for k in range(a - 1, 0, -1):
    L, R = tree[2*k], tree[2*k + 1]
    if L[0] < R[0] or (L[0] == R[0] and L[1] < R[1]):
        tree[k] = L
    else:
        tree[k] = R
def bd(arr, n):
    t = [0] * (2 * n)
    for i in range(n):
        t[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        t[i] = t[2*i] + t[2*i+1]
    return t

def query(tree, n, l, r):
    l += n; r += n
    res = 0
    while l <= r:
        if l & 1:
            res += tree[l]; l += 1
        if not (r & 1):
            res += tree[r]; r -= 1
        l //= 2; r //= 2
    return res

last = bd(li, a)
def update(tree, n, idx, value):
    aa = n + idx
    tree[aa] = (value, idx)
    aa //= 2
    while aa:
        f, l = tree[2*aa], tree[2*aa + 1]
        if f[0] < l[0] or (f[0] == l[0] and f[1] < l[1]):
            tree[aa] = f
        else:
            tree[aa] = l
        aa //= 2


for i in range(b):
    lili = list(map(int, input().split()))
    if lili[0] == 1:
        update(tree, a, lili[1] - 1, lili[2])
    else:

        print(tree[1][1] + 1)
