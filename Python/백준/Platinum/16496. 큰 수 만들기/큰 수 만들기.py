from functools import cmp_to_key

a=int(input())
li=list(map(str,input().split()))
def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0
li.sort(key=cmp_to_key(compare))
if li[0]=="0":
    print(0)
    exit()
for i in li:
    print(i,end="")
