INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

for i in range(1, N + 1):
    for j in range(1, N +1):
        if i == j:
            graph[i][j] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = 0
count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if (graph[i][j] != 0 and graph[i][j] != INF) or (graph[j][i] != 0 and graph[j][i] != INF):
            count += 1  
    if count == N - 1:
        result += 1
    count = 0

print(result)
        

