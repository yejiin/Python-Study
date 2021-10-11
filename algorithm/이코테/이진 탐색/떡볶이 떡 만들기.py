# 1부터 가장 긴 떡의 길이까지 이진 탐색. 중간값을 절단기에 설정한 높이
# target은 요청한 길이 M
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        total_length = 0 
        
        for i in array:
            if i > mid:
                total_length += i - mid
        if total_length == target:
            return mid
        # 절단한 떡의 총 길이가 요청한 길이보다 길다면 높이가 더 커야한다.
        elif total_length > target:
            start = mid + 1
        else:
            end = mid - 1
        total_length = 0

N, M = map(int, input().split())

array = list(map(int, input().split()))

print(binary_search(array), 6, 1, max(array))