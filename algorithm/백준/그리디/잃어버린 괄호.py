data = input()


sum_list = []  # 괄호로 묶인 값들끼리 더하고, 괄호로 묶이지 않은 값들끼리 더해서 리스트에 음수로 저장
num_data = []  # 숫자 데이터는 리스트에 넣어서 숫자로 변환
result = 0  # 괄호로 묶이거나, 묶이지 않은 값들을 더하여 저장하기 위한 변수

for i in range(len(data)):
    if data[i].isnumeric(): 
        num_data.append(data[i])
    else:
        for j in range(len(num_data)):
            result += int(num_data[j]) * (10 ** (len(num_data) - j - 1))  # num_data를 숫자로 변환해서 result에 저장
        if data[i] == '-':
            sum_list.append(-result)
            result = 0
        num_data = []

# 마지막 숫자 데이터 연산
idx = 1
for i in num_data:
    result += int(i) * (10 ** (len(num_data) - idx)) 
    idx += 1

sum_list.append(-result)
sum_list[0] = -sum_list[0]  # 첫번째 데이터도 음수로 저장되어 있기 때문에 양수로 변환 

print(sum(sum_list))

