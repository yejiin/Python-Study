def solution(answers):
    answer = []
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0] * 3
    
    for i in range(1, len(answers) + 1):
        if answers[i - 1] == pattern1[(i - 1) % len(pattern1)]:
            score[0] += 1
        if answers[i - 1] == pattern2[(i - 1) % len(pattern2)]:
            score[1] += 1
        if answers[i - 1] == pattern3[(i - 1) % len(pattern3)]:
            score[2] += 1
    
    max_result = max(score)

    for i in range(0, 3):
        if max_result == score[i]:
            answer.append(i + 1)
    # for idx, i in enumerate(score):
    #     if i == max(score):
    #         answer.append(idx + 1)

    return answer
    