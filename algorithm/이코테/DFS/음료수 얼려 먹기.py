N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int,input())))

def dfs(x, y):
    # 범위 넘어가면 False
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 상, 하, 좌, 우 순으로 스택에 push. 방문한 경우 False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        # 방문하지 않은 묶음을 처음 방문했을 때 True 반환 
        # (ex. (0, 0),(0, 1) 가 0 이었다면 (0, 0)을 본다면 (0, 0)과 (0, 1)이 1로 채워진다. 다음에 (0, 1)을 본다면 이미 1로 채워졌기 때문에 False)
        if dfs(i, j) == True:
            result += 1

print(result)