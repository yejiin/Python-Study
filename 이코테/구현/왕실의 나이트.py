input_data = input()

row = int(input_data[1])
# 문자를 숫자로 변경해서 사용
column = int(ord(input_data[0]) - ord('a')) + 1

# 튜플 ( ), 이동할 수 있는 모든 경우
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
