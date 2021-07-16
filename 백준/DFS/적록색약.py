import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = []

data_1 = ['R', 'G', 'B']
data_2 = [['R', 'G'], ['B']]

for _ in range(n):
    graph.append(input())

visited_1 = [[0] * n for _ in range(n)]
visited_2 = [[0] * n for _ in range(n)]

def dfs_1(x, y, color, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] in color and visited[x][y] == 0:
        visited[x][y] = 1
        dfs_1(x - 1, y, color, visited)
        dfs_1(x, y - 1, color, visited)
        dfs_1(x + 1, y, color, visited)
        dfs_1(x, y + 1, color, visited)
        return True
    return False

result_1 = 0
result_2 = 0
for i in range(n):
    for j in range(n):
        for k in data_1:
            if dfs_1(i, j, k, visited_1) == True:  
                result_1 += 1
        for l in data_2:
            if dfs_1(i, j, l, visited_2) == True:
                result_2 += 1

print(result_1, result_2)