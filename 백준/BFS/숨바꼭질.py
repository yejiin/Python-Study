from collections import deque

INF = int(1e9)

n, k = map(int, input().split())

data = [INF] * 100001

q = deque()
q.append((n, 0))

while q:
    x, c = q.popleft()    

    if x > 100000 or x < 0:
        continue    
    if data[x] < c:
        continue

    data[x] = c

    q.append((x - 1, c + 1))
    q.append((x + 1, c + 1))
    q.append((x * 2, c + 1))

print(data[k])