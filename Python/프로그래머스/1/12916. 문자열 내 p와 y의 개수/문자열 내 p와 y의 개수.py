def solution(s):
    answer = True
    s=list(s)
    print(s)
    pc=0
    yc=0
    for i in s:
        if i=="p" or i=="P":
            pc+=1
        elif i=="y" or i=="Y":
            yc+=1
    print(pc,yc)
    if pc!=yc:
        answer=False
    return answer