from collections import deque

m, n = map(int, input().split())

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 들어있지 않은 칸
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs():

    global result

    queue = deque()

    # graph에서 1인 좌표를 큐에 먼저 넣기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j, 0))

    while queue:
        
        # c: 일수
        x, y, c = queue.popleft()

        result = max(result, c)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny, c + 1))

bfs()

flag = False
for i in range(n):
    if 0 in graph[i]:
        flag = True

if flag:
    print(-1)
else:
    print(result)