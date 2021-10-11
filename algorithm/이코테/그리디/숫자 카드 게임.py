N, M = map(int, input().split())

# Python에서는 2차 배열로 입력 받을 필요 없음
# 한 줄씩 입력 받아 사용
lst = []

for i in range(0, N):
    lst.append([])
    a = list(map(int,input().split()))
    lst[i] = a

# 가장 작은 값, 가장 큰 값 구할 때 min(), max() 함수 사용하기
result = 0

for i in range(N):
    lowest = lst[i][0]  
    for j in range(M): 
        if(lowest > lst[i][j]):
            lowest = lst[i][j]
    if(lowest > result):
        result = lowest

print(result)   