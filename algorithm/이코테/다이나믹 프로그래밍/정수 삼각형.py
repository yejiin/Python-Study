n = int(input())

data = []

for i in range(n):
    data_list = list(map(int, input().split()))
    for j in range (n, i + 1, -1):
        data_list.append(0)
    data.append(data_list)

for i in range(n):
    for j in range(n):
        # 위에서 오는 경우
        if i == 0:
            up =  0
        else:
            up = data[i-1][j]
        # 왼쪽 위에서 오는 경우
        if i == 0:
            left_up = 0
        else:
            left_up = data[i-1][j-1]
        data[i][j] = data[i][j] + max(up, left_up)

print(max(data[n-1]))

