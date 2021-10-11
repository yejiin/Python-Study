N = int(input())

data = list(map(int, input().split()))

start = 0
end = len(data) -1
result =0

while start <= end:
    mid = (start + end) // 2
    # 고정점인지 확인
    if data[mid] == mid:
        result = mid
        break
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
    result = -1

print(result)