import sys
sys.setrecursionlimit(10**6)

result = 0

def dfs(i, value, numbers, target):
    global result
    if i == len(numbers):
        if value == target:
            result += 1
    else:
        dfs(i + 1, value + numbers[i], numbers, target)
        dfs(i + 1, value - numbers[i], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return result