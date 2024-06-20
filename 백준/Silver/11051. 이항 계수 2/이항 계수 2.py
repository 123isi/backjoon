import sys

def compute_combinations(n, k):
    comb = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                comb[i][j] = 1
            else:
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % 10007
    
    return comb[n][k]

def main():
    input = sys.stdin.read()
    x, y = map(int, input.split())
    result = compute_combinations(x, y)
    
    print(result)

if __name__ == "__main__":
    main()
