def solution(n):
    answer = 0
    data = sorted(list(map(int, str(n))))
    for i in range(len(data)):
        answer += data[i] * (10 ** i) 
    return answer

    # 문자열 합치는 join() 함수를 사용한 풀이
    # data = sorted(list(str(n)), reverse=True)
    # return int("".join(data))
