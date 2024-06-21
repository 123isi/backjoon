import sys
x=int(sys.stdin.readline())
li=[]
for i in range(x):
    li.append(int(input()))
li.sort()
li.reverse()
for i in li:
    print(i)