# 1부터 n까지 문제 조건의 연산을 사용하는 횟수의 최솟값을 d에 저장
n = int(input())

d = [0] * (10 ** 6 + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1  #(조건) 3. 1을 뺀다
    if i % 2 == 0:  # 2. 2로 나누어 떨어지면, 2로 나눈다.
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:  # 1. 3으로 나누어 떨어지면, 3으로 나눈다. 
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])