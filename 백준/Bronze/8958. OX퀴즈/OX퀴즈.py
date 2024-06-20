x = int(input())
for i in range(x):
    a=input()
    score=0
    b=0
    for j in a:
        if j=='O':
            score+=1
        else:
            score=0
        b+=score
    print(b)