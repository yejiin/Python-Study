N, K = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse=True)

for i in range(K):
    if(A_list[i] < B_list[i]):
        A_list[i], B_list[i] = B_list[i], A_list[i]
    else:
        break

print(sum(A_list))

