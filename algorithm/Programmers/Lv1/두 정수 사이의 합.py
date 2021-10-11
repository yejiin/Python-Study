def solution(a, b):
    answer = 0

    if a < b:
        #answer = sum(range(a, b + 1))
        for i in range(a, b + 1):  
            answer += i
    else:
        #answer = sum(range(b, a + 1))
        for i in range(b, a + 1):
            answer += i
    return answer