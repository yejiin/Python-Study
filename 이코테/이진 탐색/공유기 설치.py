n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

# 첫번째 집에 공유기 설치, 공유기 사이의 최소 거리, 최대 거리
min_gap = 1
max_gap = data[-1] - data[0]
result = 0

while (min_gap <= max_gap):
    gap = (min_gap + max_gap) // 2  
    value = data[0]
    count = 1

    # gap을 이용해 공유기 설치
    for i in range(1, n):
        if data[i] >= value + gap:
            value = data[i]
            count += 1

    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우. 거리 증가
        min_gap = gap + 1
        result = gap
    else:  # c개 이상의 공유기를 설치할 수 없는 경우. 거리 감소
        max_gap = gap - 1

print(result)