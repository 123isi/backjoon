def solution(s):
    answer = True
    arr=[]
    li=list(s)
    for i in li:
        if i=="(":
            arr.append(1)
        else:
            if arr==[]:
                answer=False
                break
            else:
                arr.pop()
    if arr!=[]:
            answer=False
    return answer