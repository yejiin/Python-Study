N = int(input())

data = list(map(int, input().split()))

data.sort()

target = 1
for i in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i

# 만들 수 없는 금액 출력
print(target)
    

