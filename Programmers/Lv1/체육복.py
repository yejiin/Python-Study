def solution(n, lost, reserve):
    answer = 0
    data = [1] * (n + 2)

    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            data[i] = 0
    
    reserve.sort()
    
    for i in reserve:
        if data[i - 1] == 0:
            data[i - 1] = 1
        elif data[i + 1] == 0:
            data[i + 1] = 1

    answer = n - data.count(0)
    return answer

