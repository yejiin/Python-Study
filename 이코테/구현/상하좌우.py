N = int(input())

data = input().split()

x = 1
y = 1

for i in data:
    if i == 'L':
    	# y좌표가 1인데 L에 따라 움직인다면 정사각형을 벗어나므로 가만히 있는다 
        if y == 1:
           continue
        print('L')
        y -= 1
    elif i == 'R':
    	# y좌표가 N인데 R에 따라 움직인다면 정사각형을 벗어나므로 가만히 있는다 
        if y == N:
           continue
        print('R')
        y += 1
    elif i == 'U':
    	 # x좌표가 1인데 U에 따라 움직인다면 정사각형을 벗어나므로 가만히 있는다 
        if x == 1:
           continue
        print('U')
        x -= 1        
    elif i == 'D':
       	# x좌표가 N인데 D에 따라 움직인다면 정사각형을 벗어나므로 가만히 있는다 
        if x == N:
           continue
        print('D')
        x += 1

print(x, y)