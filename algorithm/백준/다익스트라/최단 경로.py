# 노드의 개수가 5,000 이상
# 힙(우선순위 큐) 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)

k = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dikjstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dikjstra(k)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])