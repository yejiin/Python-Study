N = int(input())

input_data = list(map(int, input().split()))

d = [0] * (N + 1)

d[1] = input_data[0]
d[2] = input_data[1]

for i in range(3, N + 1):
    max_val = 0
    for j in range(i - 2, 0, -1):
        temp = d[j] + input_data[i-1]
        max_val = max(max_val, temp)
    d[i] = max_val

print(max(d[-1],d[-2]))