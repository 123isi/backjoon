def solution(s):
    li = list(s.split(' '))
    arr = []
    li2 = []

    for i in li:
        if i:
            arr = list(i.lower())
            arr[0] = arr[0].upper()
            li2.append(''.join(arr))
        else:
            li2.append('')

    answer = ' '.join(li2)
    return answer