# 반복문을 사용하여 이진 탐색 구현
def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 재귀 함수를 사용하여 이진 탐색 구현
def binary_search2(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search2(array, target, start, mid - 1)
    else:
        return binary_search2(array, target, mid + 1, end)