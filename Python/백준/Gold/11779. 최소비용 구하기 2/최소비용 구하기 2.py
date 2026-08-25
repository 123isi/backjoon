import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
path = [0] * (n + 1)  # 이전 도시를 저장할 리스트 추가

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
                path[next_node] = now  # 직전 노드 기록 (중요!)

a, b = map(int, input().split())
dijkstra(a)

# 경로 역추적
route = []
a = b
while a != 0:
    route.append(a)
    a = path[a]

route.reverse()  # 출발점부터 도착점까지 순서로 변경

# 출력 (문제의 요구사항에 맞게 출력)
print(distance[b])
print(len(route))
print(*route)
