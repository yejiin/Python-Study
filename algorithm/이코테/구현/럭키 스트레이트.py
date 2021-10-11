N = input()

# 입력된 N의 길이의 절반의 크기
N_half = len(N) // 2

# 왼쪽 부분을 int형으로 바꾸고, 리스트로 변환
left = list(map(int, N[:N_half]))
# 오른쪽 부분을 int형으로 바꾸고, 리스트로 변환
right = list(map(int, N[N_half:]))

if (sum(left) == sum(right)):
    print("LUCKY")
else:
    print("READY")

