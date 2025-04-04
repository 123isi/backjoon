x = int(input())
while x > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    x -= 1
