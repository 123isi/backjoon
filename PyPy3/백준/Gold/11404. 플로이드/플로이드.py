a = int(input())  # 정점의 수
b = int(input())  # 간선의 수
li = [[float('inf')] * a for _ in range(a)]  # 초기화: 모든 경로를 무한대로 설정

# 간선 정보 입력
for _ in range(b):
    x, y, z = map(int, input().split())
    li[x - 1][y - 1] = min(li[x - 1][y - 1], z)  # 간선 비용 설정

# 대각선(자기 자신으로 가는 경로)을 0으로 초기화
for i in range(a):
    li[i][i] = 0

# 플로이드 워셜 알고리즘 수행
for k in range(a):  # 경유지
    for i in range(a):  # 출발지
        for j in range(a):  # 도착지
            li[i][j] = min(li[i][j], li[i][k] + li[k][j])

# 결과 출력
for i in range(a):
    row = li[i]
    arr = []
    for x in row:
        if x == float('inf'):
            arr.append('0')  # 도달할 수 없는 경우
        else:
            arr.append(str(x))
    a = " ".join(arr)
    print(a)
