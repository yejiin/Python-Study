def solution(absolutes, signs):
    answer = 0
    for i in zip(absolutes, signs):
        if i[1] == False:
            answer -= i[0]
        else:
            answer += i[0]
    return answer

    # return sum(-i[0] if i[1] == False else i[0] for i in zip(absolutes, signs))