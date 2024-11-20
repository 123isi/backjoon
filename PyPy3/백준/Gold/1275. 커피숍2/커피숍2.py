a, b = map(int, input().split())
li = list(map(int, input().split()))

def bd(arr, n):
    tree = [0] * (2 * n)
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    return tree

def update(tree, n, idx, value):
    idx += n
    tree[idx] = value
    while idx > 1:
        idx //= 2
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

def query(tree, n, l, r):
    l += n
    r += n
    result = 0
    while l <= r:
        if l % 2 == 1:
            result += tree[l]
            l += 1
        if r % 2 == 0:
            result += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return result
last = bd(li, a)

for _ in range(b):
    z, g, d, w = map(int, input().split())
    z, g = min(z, g), max(z, g)
    print(query(last, a, z - 1, g - 1))
    update(last, a, d - 1, w)
