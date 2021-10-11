N = int(input())

result = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            # 두자리 숫자는 '3'이 포함되어 있는지 확인하기 어려우므로 문자열로 바꿔서 확인
            # in 키워드, find() 함수를 사용하여 특정 문자열 포함되어 있는지 확인
            if '3' in str(i) + str(j) + str(k):
                result += 1     

print(result)

