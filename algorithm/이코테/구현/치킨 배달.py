from itertools import combinations

n, m = map(int, input().split())

chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# 조합 사용해서 모든 치킨집 중에서 m개의 치킨집 고름 
candidates = list(combinations(chicken, m))

# 치킨 거리의 합 계산 함수
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)