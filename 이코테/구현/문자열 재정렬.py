data = input()

number_sum = 0
Alphabet_list =[]

# 숫자 0 ~ 9 아스키 코드 값 => 48 ~ 57
# 알파벳 대문자 A ~ Z 아스키 코드 값 => 65 ~ 90
for i in data:
    if i.isdigit():
        number_sum += int(i)
    else:
        Alphabet_list.append(i)

Alphabet_list.sort()

# join 함수. 리스트의 문자열들을 합치는 역할
print(''.join(Alphabet_list), end=str(number_sum))
