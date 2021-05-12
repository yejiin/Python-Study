def solution(x):
    answer = True

    data = list(map(int,str(x)))
    data_sum = sum(data)

    if x % data_sum != 0:
        answer = False
    return answer