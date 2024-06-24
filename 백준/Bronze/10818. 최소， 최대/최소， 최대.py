x=int(input())
li=list(map(int,input().split()))
li.sort()
print(li[0],li[x-1])