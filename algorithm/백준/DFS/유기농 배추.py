import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y -1)
        dfs(x, y + 1)
        return True
    return False

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for i in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    result = 0      
    for i in range(N):
        for j in range(M):
            if dfs(j, i) == True:
                result += 1
    print(result)

