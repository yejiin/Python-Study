data = input().split(' ')

count = 0
for i in data:
    if i == '':
        count += 1 

print(len(data) - count)
