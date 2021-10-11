def solution(s):
    # 압축한 문자열의 길이가 가장 큰 경우는 문자열이 압축되지 않았을 때
    answer = len(s)

    # 자를 수 있는 단위는 문자열의 길이의 절반까지 (ex. len(s)=8, 4개 단위까지)
    for i in range(1, len(s) // 2 + 1):
        target = s[0:i]
        compressed = ''
        count = 1
        for j in range(i, len(s), i):
            if target == s[j:j+i]:
                count += 1
            else:
                compressed += str(count) + target if count >= 2 else target
                target = s[j:j+i]
                count = 1
        compressed += str(count) + target if count >= 2 else target
        answer = min(answer, len(compressed))
    return answer
