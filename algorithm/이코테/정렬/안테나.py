N = int(input())

home_loc = list(map(int, input().split()))

home_loc.sort()

print(home_loc[len(home_loc)//2-1])