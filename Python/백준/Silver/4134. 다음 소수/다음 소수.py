import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

a = int(input())
li = [int(input()) for _ in range(a)]

for i in li:
    if i <= 1:
        print(2)
    else:
        re = i
        while True:
            if is_prime(re):
                print(re)
                break
            re += 1
