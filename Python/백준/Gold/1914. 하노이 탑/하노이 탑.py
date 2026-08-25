import math

def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
    else:
        hanoi(n-1, a, c, b)
        print(f"{a} {c}")
        hanoi(n-1, b, a, c)

def main():
    n = int(input())
    temp = int(math.pow(2, n)) - 1
    print(temp)
    if n <= 20:
        hanoi(n, 1, 2, 3)

if __name__ == "__main__":
    main()
