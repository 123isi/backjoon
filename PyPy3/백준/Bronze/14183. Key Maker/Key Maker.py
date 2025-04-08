import sys
input = sys.stdin.readline

while True:
    m_n = input()
    if not m_n:
        break
    m, n = map(int, m_n.strip().split())
    if m == 0 and n == 0:
        break

    c = list(map(int, input().strip().split()))
    t = []
    for _ in range(n):
        t.append(list(map(int, input().strip().split())))

    ans = 0
    for i in range(n):
        ok = True
        for j in range(m):
            if c[j] < t[i][j]:
                ok = False
                break
        if ok:
            ans += 1

    print(ans)
