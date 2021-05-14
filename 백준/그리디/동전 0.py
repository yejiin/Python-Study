N, K = map(int, input().split())

A = [] * N

for _ in range(N):
    A.append(int(input()))

A.sort(reverse=True)

result = 0
for i in A:
    if i > K:
        continue
    else:
        result += K // i
        K = K % i

print(result)