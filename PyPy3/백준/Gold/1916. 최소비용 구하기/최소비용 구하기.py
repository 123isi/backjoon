import heapq
import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력받기
n = int(input())
m = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for b, cost in graph[now]:
            new_cost = dist + cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if new_cost < distance[b]:
                distance[b] = new_cost
                heapq.heappush(q, (new_cost, b))

# 다익스트라 알고리즘 수행
a, b = map(int, input().split())
dijkstra(a)

# 출발 노드 a에서 도착 노드 b까지의 최단 거리 출력
print(distance[b])
