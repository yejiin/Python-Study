data = input()

result = 0
flag = 0

# 0과 1이 나온 숫자 다음에만 더하기 연산을 한다. 나머지는 곱하기 연산
for i in data:
    # 앞문자가 0 또는 1인지 아닌지 flag가 담고 있기 때문에 flag 값에 따라 연산 수행
    if flag == 0:
        result += int(i)
    else :
        result *= int(i)
    # 문자가 0 또는 1이면 flag = 0, 아니면 flag = 1
    if int(i) == 0 or int(i) == 1:
        flag = 0
    else:
        flag = 1

print(result)