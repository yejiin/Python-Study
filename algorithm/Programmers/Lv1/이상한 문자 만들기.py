def solution(s):
    answer = ''
    lst = list(s.split(' '))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2 == 0:
                answer +=lst[i][j].upper()
            else:
                answer += lst[i][j].lower()

    #return answer[0:-1]
        if i != len(lst) - 1:    
            answer += ' '    
    return answer