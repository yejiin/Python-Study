import sys
sys.setrecursionlimit(100000)

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for a in range(1, k + 1):
    n1, m1, n2, m2 = map(int, input().split())

    for i in range(m1, m2):
        for j in range(n1, n2):
            graph[i][j] = 1

def dfs(x, y):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        cnt += 1
        return cnt
    return 0

result = 0
weight = []
for i in range(m):
    for j in range(n):
        cnt = 0
        cc = dfs(i, j)
        if cc != 0:
            weight.append(cc)
            result += 1

weight.sort()
print(result)
for i in weight:
    print(i, end = ' ')