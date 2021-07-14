import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = []
max_value = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_value = max(max_value, max(graph[i]))

def dfs(x, y, k, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == 1:
        return False
    if graph[x][y] > k and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x - 1, y, k, visited)
        dfs(x, y - 1, k, visited)
        dfs(x + 1, y, k, visited)
        dfs(x, y + 1, k, visited)
        return True
    return False

max_result = 0
for k in range(max_value):
    visited = [[0] * n for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(n):
            if dfs(i, j, k, visited) == True:
                result += 1
    max_result = max(result, max_result)
    
print(max_result)