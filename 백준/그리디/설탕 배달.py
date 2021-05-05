N = int(input())

cnt_5_temp = N // 5

data = N
result = 0
flag = False

for cnt_5 in range(cnt_5_temp, -1, -1):
    data -= 5 * cnt_5
    if data % 3 == 0 :
        cnt_3 = data // 3
        result = cnt_5 + cnt_3
        flag = True
        break
    data = N

if flag == False:
    print(-1)
else:   
    print(result)