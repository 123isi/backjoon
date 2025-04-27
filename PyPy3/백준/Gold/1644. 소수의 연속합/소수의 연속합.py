

a = int(input())
li = []
for i in range(2, a+1):
    p = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            p = False
            break
    if p:
        li.append(i)

count = 0
start = 0
end = 0
sum = 0

while True:
    if sum >= a:
        if sum == a:
            count += 1
        sum -= li[start]
        start += 1
    else:
        if end == len(li):
            break
        sum += li[end]
        end += 1

print(count)
