n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y, z):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = z
        dfs(x - 1, y, z)
        dfs(x, y - 1, z)
        dfs(x + 1, y, z)
        dfs(x, y + 1, z)
        return True
    return False

result = 0  # result는 단지수
z = 2  # z는 단지 번호. 0, 1번이 집 여부를 나타내므로 단지 번호는 2부터 시작하게 하였다.
for i in range(n):
    for j in range(n):
        if dfs(i, j, z) == True:
            z += 1
            result += 1

result_num = [0 * i for i in range(result)]

for i in range(n):
    for j in range(2, 2 + result):
        result_num[j-2] += graph[i].count(j)

result_num.sort()

print(result)
for i in result_num:
    print(i)
