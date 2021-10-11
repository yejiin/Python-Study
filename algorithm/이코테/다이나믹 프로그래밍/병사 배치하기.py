N = int(input())

data = list(map(int, input().split()))

data.reverse()

d = [1] * N

for i in range(1,N):
    for j in range(0, i):
        if data[j] < data[i]:
            d[i] = max(d[i], d[j] + 1)
   
print(N - max(d))


