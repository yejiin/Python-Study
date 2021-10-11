def solution(numbers):
    data = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            data.append(numbers[i]+numbers[j])
    answer = sorted(list(set(data)))
    
    return answer