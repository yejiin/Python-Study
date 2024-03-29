import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for T in range(int(input())):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[N-1][N-1])

