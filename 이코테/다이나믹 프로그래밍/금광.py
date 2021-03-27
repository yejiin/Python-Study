def gold_func(n, m, data):

    d = [[0] * m for _ in range(n)] 

    for i in range(n):
        d[i][0] = data[i][0]
        
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 아래가 금광 범위를 넘지 않는다면
            if i+1 < n:
                temp = data[i][j] + d[i+1][j-1]
                d[i][j] = max(d[i][j], temp)
            # 왼쪽 위가 금광 범위를 넘지 않는다면
            elif i-1 >= 0:
                temp = data[i][j] + d[i-1][j-1]
                d[i][j] = max(d[i][j], temp)
            # 왼쪽
            temp = data[i][j] + d[i][j-1]
            d[i][j] = max(d[i][j], temp)
    max_list = []

    for i in range(n):
        max_list.append(max(d[i]))

    print(max(max_list))
    

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    input_data = list(map(int, input().split()))
    
    data = []

    for i in range(0,len(input_data),m):
        data.append(input_data[i:i+m])

    gold_func(n, m, data)
