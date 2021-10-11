from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    # 간선은 양방향이므로 노드 리스트에 각각 추가
    graph[a].append(b)
    graph[b].append(a)


# 정점 번호가 작은 것부터 먼저 방문하므로 정렬
for i in range(1, N+1):
    graph[i].sort()

visited_b = [False] * (N+1)

def bfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            bfs(graph, i, visited)

visited_d = [False] * (N+1)

def dfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        visited_d[now] = True
        for i in graph[now]:
            if visited_d[i] == False:
                queue.append(i)
                visited_d[i] = True

    
bfs(graph, V, visited_b)
print()
dfs(V)