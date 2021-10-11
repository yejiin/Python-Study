def solution(d, budget):
    answer = 0
    d.sort()

    total = 0
    for i in d:
        total += i
        if total <= budget:
            answer += 1
        else :
            break

    return answer