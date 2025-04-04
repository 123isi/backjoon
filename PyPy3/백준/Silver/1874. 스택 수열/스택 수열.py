import sys

input = sys.stdin.readline

li = []
cnt = 1

arr=[]
for i in range(int(input())):
    x = int(input())
    while cnt <= x:
        li.append(cnt)
        arr.append('+')
        cnt += 1
    if x == li[-1]:
        li.pop()
        arr.append('-')
    else:
        print('NO')
        exit()
for i in arr:
    print(i)
