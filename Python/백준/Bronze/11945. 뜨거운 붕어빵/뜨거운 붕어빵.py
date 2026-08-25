a, b = map(int, input().split())
for i in range(a):
    a = input()
    li = list(a)
    li.reverse()
    li = ''.join(li)
    print(li)
