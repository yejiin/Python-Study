def solution(N, stages):
    stage_count = [0] * (N+1)
    for stage in stages:
        stage_count[stage-1] += 1

    fail_rate = [0] * N
    front_user = 0
    fail_rate[0] = (stage_count[0]/len(stages),1)

    for i in range(1, len(stage_count)-1):
        front_user += stage_count[i-1]
        
        # 사용자가 높은 스테이지까지 도달하지 못한 경우 스테이지에 도달한 플레이어의 수가 0이므로 실패율을 0으로 정해준다. 
        if len(stages) - front_user != 0:
            fail_rate[i] = (stage_count[i]/(len(stages) - front_user), i+1)
        else:
           fail_rate[i] = (0, i+1)

    result = sorted(fail_rate[:N],key= lambda x: x[0], reverse=True)
    answer = [i[1] for i in result]

    return answer

