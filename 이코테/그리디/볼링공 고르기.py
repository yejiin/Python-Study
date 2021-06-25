n, m = map(int, input().split())
data = list(map(int, input().split()))

# 아래 코드보다 더 효율적
# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]  # A가 선택할 수 있는 개수 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기



# 이중 반복문으로 모든 경우의 수 계산 
# weight = list(map(int, input().split()))
# result = 0

# for i in range(n):
#     for j in range(i + 1, n):
#         if weight[i] != weight[j]:
#             result += 1

# print(result)

