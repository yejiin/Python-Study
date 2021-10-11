from collections import deque

N, M = map(int, input().split())
miro_map = []

for i in range(N):
    miro_map.append(list(map(int,input())))

step = [(-1,0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 모두 방문
        for i in range(4):
            nx = x + step[i][0]
            ny = y + step[i][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if miro_map[nx][ny] == 0:
                continue
            # 다음 노드가 처음 방문 한 경우, 현재 노드보다 거리가 한 칸 더 멀다
            if miro_map[nx][ny] == 1:
                miro_map[nx][ny] = miro_map[x][y] + 1
                queue.append((nx, ny))

    return miro_map[N-1][M-1]

print(bfs(0,0))

    