N, M, K = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort(reverse=True)

result = 0

i=0

while True:
    for j in range(0, K):
        if(i == M):
            break
        result += lst[0]
        i = i + 1
    if(i == M):
        break
    result += lst[1]
    i = i + 1
    
print(result)
