def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
data = list(map(int, input().split()))
for i in data:
    if binary_search(array, i, 0, n - 1) == None:
        print(0)
    else:
        print(1)