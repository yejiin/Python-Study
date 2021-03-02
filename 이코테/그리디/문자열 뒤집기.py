import math

data = input()

# 변경 되는 지점 수
count = 0

comp = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    # 앞 데이터와 일치하지 않을 때 comp 변수를 다시 바꿔준다.
    if comp != num:
        count += 1
        comp = num

# 뒤집기 횟수는 count를 나누기 2한 수이다. count가 홀수 일 때는 올림 
result = math.ceil(count / 2)
print(result)