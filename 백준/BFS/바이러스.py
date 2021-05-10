from collections import deque

v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    # 양방향 그래프
    graph[a].append(b)
    graph[b].append(a)  

visited = [False] * (v+1)

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(1)
if visited[1] == True:  # 1번 컴퓨터는 결과값에서 제외되어야 한다.
    print(visited.count(True) - 1)
else:
    print(visited.count(True))

