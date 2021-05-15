N, M = map(int, input().split())

tree = list(map(int, input().split()))

def binary_search(target, start, end):
    result_max = 0  # 나무 높이의 합이 정확히 M으로 떨어지지 않을 때 최댓값
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in tree:
            if i > mid:
                result += i - mid
        if result == target:
            return mid
        elif result > target :
            result_max = mid
            start = mid + 1
        else :
            end = mid - 1
    return result_max

print(binary_search(M, 0, max(tree)))
