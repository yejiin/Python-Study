def solution(n, m):
    answer = []
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            a1 = i
    answer.append(a1)
    a2 = m
    while True:
        if a2 % n == 0 and a2 % m == 0:
            answer.append(a2)
            break
        a2 += 1
    return answer