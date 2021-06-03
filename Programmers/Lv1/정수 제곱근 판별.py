import math

def solution(n):
    answer = 0
    # math.sqrt(n) == n ** (1/2)
    data = math.sqrt(n)
    if (data % 1) == 0:
        answer = (int(data) + 1) ** 2
    else :
        answer = -1 

    return answer