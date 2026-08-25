import sys
input = sys.stdin.readline
memo = [-1] * 136
def fibo(a):
    if a <= 3:
        return 1
    if memo[a] != -1: 
        return memo[a]
    memo[a] = fibo(a-1) + fibo(a-3)
    return memo[a]

a = int(input())
print(fibo(a))
