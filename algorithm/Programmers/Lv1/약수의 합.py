def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

    # 위 코드를 한 줄로
    # return sum([i for i in range(1, n + 1) if n % i == 0])