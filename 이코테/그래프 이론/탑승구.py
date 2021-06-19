def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parnet(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 탑승구 번호
g = int(input())

# 비행기 개수
p = int(input())

# 탑승구
graph = []

for i in range(g + 1):
    graph.append(i)

result = 0 
for _ in range(p):
    data = find_parent(graph, int(input()))  # 현재 비행기의 탑승구의 루트 확인

    if data == 0:  # 현재 루트가 0이라면, 종료
        break

    union_parnet(graph, data, data - 1)  # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)