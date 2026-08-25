x, y = int(input()), input()
cnt = 0

for i in range(x // 2):
    left = y[i]
    right = y[x - i - 1]

    if left == right:
        if left == '?':
            cnt += 26  
    else:
        if left == '?' or right == '?':
            cnt += 1   
        else:
            print(0)
            exit()

print(cnt)
