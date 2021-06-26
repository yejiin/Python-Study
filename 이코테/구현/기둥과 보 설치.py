# 현재 설치된 구조물이 가능한 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥인 경우
            # '바닥 위' 또느 '보의 한쪽 끝부분 위' 또는 '다른 기둥 위'라면 가능
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 보인 경우
            # '한쪽 끝부분이 기둥 위' 또는 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 가능
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operation = frame
        if operation == 0:  # 삭제하는 경우
            answer.remove([x, y, stuff])  # 일단 삭제
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.append([x, y, stuff])  # 불가능하면 다시 설치
        if operation == 1:  # 설치하는 경우
            answer.append([x, y, stuff])  # 일단 설치
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])  # 불가능하면 다시 제거

    return sorted(answer)


build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(5, build_frame))