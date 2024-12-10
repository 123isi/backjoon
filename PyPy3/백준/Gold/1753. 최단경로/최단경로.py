import heapq
import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 구현 (우선순위 큐 사용)
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 처리된 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue

        # 현재 노드와 연결된 다른 노드들을 확인
        for b, c in graph[now]:
            cost = dist + c
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, INF 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
