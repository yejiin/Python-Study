import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

x = []
y = []
z = []

for i in range(1, n + 1):
    inx, iny, inz = map(int, input().split())
    x.append((inx, i))
    y.append((iny, i))
    z.append((inz, i))

x.sort()
y.sort()
z.sort()

# x축만 존재했을 때, y축만 존재했을 때, z축만 존재했을 때 가정. N - 1 간선 
for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)





# 간선을 모두 확인하는 방법 -> 메모리 초과
# 간선의 개수는 총 N(N - 1) / 2개가 될 수 있으므로 입력 조건의 최대 100,000이라는 점을 감안하면 이 방법으로는 해결 불가능

# vertexs = []

# for i in range(n):
#     x, y, z = map(int, input().split())
#     vertexs.append((x, y, z))

# edges = []
# result = 0

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         data = min(abs(vertexs[i][0] - vertexs[j][0]), abs(vertexs[i][1] - vertexs[j][1]), abs(vertexs[i][2] - vertexs[j][2]))
#         edges.append((data, i, j))

# edges.sort()
# for edge in edges:
#     cost, x, y = edge
#     if find_parent(parent, x) != find_parent(parent, y):
#         union_parent(parent, x, y)
#         result += cost

# print(result)