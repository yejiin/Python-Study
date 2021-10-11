from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 하지 않은 도시는 -1로 표시(distance[0]은 사용하지 않음)
distance = [-1] * (N+1)
distance[X] = 0

queue = deque()
queue.append(X)

while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

if K not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)