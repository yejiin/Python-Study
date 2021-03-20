# from bisect import bisect_left, bisect_right

# x의 첫 번째 위치 구하기
def binary_search_start(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if mid - 1 < 0 or array[mid - 1] != target:
                return mid
            else:
                end = mid - 1 
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# x의 마지막 위치 구하기
def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if mid + 1 >= len(array) or array[mid + 1] != target:
                return mid
            else:
                start = mid + 1 
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

N, x = map(int, input().split())
array = list(map(int, input().split()))

if binary_search_start(array, x, 0, len(array)-1) == -1 :
        print(-1)
else:
    print(binary_search_end(array, x, 0, len(array)-1) - binary_search_start(array, x, 0, len(array)-1) + 1)



# bisect 라이브러리 사용
# count = bisect_right(array, x) - bisect_left(array, x)
# if count == 0:
#     print(-1)
# else:
#     print(count)
