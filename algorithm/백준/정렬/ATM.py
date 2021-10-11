n = int(input())

p = sorted(list(map(int, input().split())))

total = 0
for i in range(len(p)):
    total += sum(p[:i+1])
print(total)