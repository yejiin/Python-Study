import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

distance = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

count = 0
time = 0
for i in range(1, len(distance)):
    if distance[i] > 0 and distance[i] < INF:
        count += 1
        temp = distance[i]
        time = max(time, temp)
print(count, end = " ")
print(time)