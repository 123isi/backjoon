a=int(input())
b=int(input())
li=list(map(int,input().split()))
if a<=sum(li):
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')