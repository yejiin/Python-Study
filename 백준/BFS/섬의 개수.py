from collections import deque
import sys
input = sys.stdin.readline

# 오른쪽부터 시계 방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(x, y, n, m):
    flag = False
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x <= -1 or x >= n or y <= -1 or y >= m:
            continue
        if graph[x][y] == 0:
            continue

        if graph[x][y] == 1:
            graph[x][y] = 2
            flag = True

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                q.append((nx, ny))
    return flag


while True:
    graph = []
    result = 0
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if bfs(i, j, h, w) == True:
                result += 1

    print(result)

