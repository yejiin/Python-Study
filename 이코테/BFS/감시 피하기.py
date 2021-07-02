# DFS/BFS 대신 조합 라이브러리 사용하여 구현
from itertools import combinations

n = int(input())
board = []  # 복도 정보
teachers = []  # 모든 선생님 위치 정보
spaces = []  # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            y -= 1

    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            y += 1

    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': 
                return True
            if board[x][y] == '0':
                return False
            x -= 1
    
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False
            x += 1
    return False

# 장애물 설치 후, 학생 감지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        board[x][y] = '0'
    if not process():
        find = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')