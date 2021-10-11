import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 버스 노선이 같다면 비용이 최솟값인 값 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c
    # if c < graph[a][b]:
    #    graph[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()