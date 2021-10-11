N = int(input())

array = []

for i in range(N):
    a, b = input().split()
    array.append((a, int(b)))

def setting(data):
    return data[1]

array = sorted(array, key=setting)

for i in array:
    print(i[0], end=' ')
