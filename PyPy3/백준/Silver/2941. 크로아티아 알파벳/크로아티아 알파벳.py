li = list(input())
a = 0
i = 0

while i < len(li):
    if i < len(li) - 1 and (li[i] + li[i + 1] in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]):
        a += 1
        i += 2 
    elif i < len(li) - 2 and li[i] == 'd' and li[i + 1] == 'z' and li[i + 2] == '=':
        a += 1
        i += 3
    else:
        a += 1
        i += 1 

print(a)
