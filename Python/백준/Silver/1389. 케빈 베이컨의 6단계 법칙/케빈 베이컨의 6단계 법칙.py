import sys
input = sys.stdin.read

# 입력 받기
data = input().splitlines()
n, m = map(int, data[0].split())  # 유저 수(N)와 친구 관계 수(M)
graph = [[float('inf')] * n for _ in range(n)]  # 초기화: 무한대로 설정

# 자기 자신으로 가는 경로는 0
for i in range(n):
    graph[i][i] = 0

# 간선 정보 입력
for i in range(1, m + 1):
    a, b = map(int, data[i].split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 각 사람의 케빈 베이컨 수 계산
result = []
for i in range(n):
    result.append(sum(graph[i]))

# 최소 케빈 베이컨 수를 가진 사람 찾기
min_value = min(result)
answer = result.index(min_value) + 1
print(answer)
