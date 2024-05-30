from collections import deque
n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]

apples = []
for _ in range(k):
    r,c = map(int,input().split())
    # arr[r-1][c-1] = 1
    apples.append((r,c))
l = int(input())
l_list = []
for _ in range(l):
    l_list.append(input().split())





def play_game(n, k, apples, l, l_list):
    arr = [[0] * n for _ in range(n)]
    for r, c in apples:
        arr[r - 1][c - 1] = 1

    directions = {int(x): c for x, c in l_list}

    time = 0
    head_d = 0  # 0: right, 1: down, 2: left, 3: up
    # Directions: right, down, left, up
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    snake = deque([(0, 0)])

    while True:
        time += 1
        head_x, head_y = snake[-1]
        nx = head_x + dx[head_d]
        ny = head_y + dy[head_d]

        if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
            return time

        snake.append((nx, ny))

        if arr[nx][ny] == 1:
            arr[nx][ny] = 0  
        else:
            snake.popleft()  

        if time in directions:
            if directions[time] == 'L':
                head_d = (head_d - 1) % 4
            else: 
                head_d = (head_d + 1) % 4

print(play_game(n, k, apples, l, l_list))