def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

x = int(input())
y = factorial(x)
y_str = str(y)


for char in reversed(y_str):
    if char != '0':
        print(char)
        break
