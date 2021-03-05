N, M = map(int,input().split())

A, B, d = map(int, input().split())

input_map = []

# 맵 입력
for i in range(N):
    input_map.append(list(map(int,input().split())))

# 이동할 수 있는 모든 경우
move_steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 바라보는 방향의 모든 경우
d_steps = [0, 1, 2, 3]

result = 0
# 캐릭터가 회전한 횟수
count = 0

# 현재 좌표 방문
input_map[A][B] = 2
result += 1

while True:
    d = d_steps[d-1]
    
    next_A = A + move_steps[d][0]
    next_B = B + move_steps[d][1]

    if input_map[next_A][next_B] == 0:
        A = next_A
        B = next_B
        input_map[A][B] = 2 
        result += 1
        count = 0
    else :
        count += 1
        #  count = 4 일 때, 네 방향 모두 확인
        if count == 4: 
            next_A = A + move_steps[d-2][0]
            next_B = B + move_steps[d-2][1]
            # 이미 가본 곳으로 이동
            if input_map[next_A][next_B] != 1:
                A = next_A
                B = next_B
                count = 0
            else:
                break

print(result)


