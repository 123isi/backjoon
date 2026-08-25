def solution(n):
    answer=[]
    while 1:
        if n<10:
            break
        answer.append(n%10)
        n=n//10

    answer.append(n)
    return answer