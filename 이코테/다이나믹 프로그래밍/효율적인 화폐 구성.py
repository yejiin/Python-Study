N, M = map(int, input().split())

d = [-1] * 10001

money = []

for i in range(N):
    x = int(input())
    money.append(x)
    d[x] = 1
    
for i in range(1, M):
    if d[i] != -1:
        for j in money:
            if d[i + j] == -1:
                d[i + j] = d[i] + 1
            else:
                d[i + j] = min(d[i + j], d[i] + 1)

print(d[M])