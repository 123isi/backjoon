x,y=map(int,input().split())
li=set(map(int,input().split()))
arr=set(map(int,input().split()))

sym_diff = (li ^ arr)
print( len(sym_diff) )
