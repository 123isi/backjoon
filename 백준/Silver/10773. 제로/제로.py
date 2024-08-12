x = int(input())
deque = []

for i in range(x):
    num = int(input())
    if(num == 0):
        deque.pop()
    else:
        deque.append(num)
print(sum(deque))
