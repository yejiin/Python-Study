N = int(input())
data = list(map(int,input().split()))

data.sort()

# 그룹 수
result = 0

# 한 그룹당 인원수
count = 0

for i in data:
    count += 1
    # 현재 인덱스의 모험가는 그룹의 인원수로 먼저 포함
    # 그룹의 인원 수는 현재 인덱스의 공포도보다 같거나 커야 그룹으로 인정된다.
    if count >= i:
        result += 1
        count = 0

print(result)


