def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] == i:
            return mid
        elif N_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
N_list = list(map(int, input().split()))

N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    result = binary_search(N_list, i, 0, N - 1)
    if result != None:
        print("yes", end=' ')
    else : 
        print("no", end=' ')


