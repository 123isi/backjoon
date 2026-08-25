import sys
input=sys.stdin.readline
a,b=map(int,input().split())
li=[]
for i in range(a):
    li.append(int(input()))
dd=a
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
tree1 = [float('inf')] * (2 * dd)
tree2 = [-1*(float('inf'))] * (2 * dd)
for i in range(dd):
    tree1[dd + i] = li[i]
    tree2[dd + i] = li[i]
for i in range(dd - 1, 0, -1):
    tree1[i] = min(tree1[2*i], tree1[2*i+1])
    tree2[i] = max(tree2[2*i], tree2[2*i+1])

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
def mimimininininininini(a,b):
    a+=dd
    b+=dd
    result=float('inf')
    while a<=b:
        if a&1:
            result=min(result,tree1[a])
            a+=1
        if not b&1:
            result=min(result,tree1[b])
            b-=1
        a//=2
        b//=2
    return result
def mamamamx(a,b):
    a += dd
    b += dd
    result = -1*float('inf')
    while a <= b:
        if a & 1:
            result = max(result, tree2[a])
            a += 1
        if not b & 1:
            result = max(result, tree2[b])
            b -= 1
        a //= 2
        b //= 2
    return result
for _ in range(b):
    aa,bb=map(int,input().split())
    aa-=1
    bb-=1
    print(mimimininininininini(aa,bb),mamamamx(aa,bb))
