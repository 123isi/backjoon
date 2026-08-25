a, b = map(int, input().split())
if a==b:
    if a==0:
        print('Not a moose')
        exit()
    print(f'Even {a*2}')
else:
    print(f'Odd {(max(a,b)*2)}')