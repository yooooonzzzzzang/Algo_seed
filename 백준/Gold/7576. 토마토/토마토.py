from collections import deque

# 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
# 열 , 행
m,n = map(int,input().split())
boxes = [list(map(int,input().split())) for _ in range(n)]

is_ripe =False



ripe_tomato = deque([])     # 익은 토마토 저장할 큐, 리스트로 pop(0) 하니까 시간초과남 ㅡㅡ
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:    # 익은 토마토
            ripe_tomato.append((i, j))

# 익은 토마토들을 시작으로 bfs 진행
while ripe_tomato:  # 값이 있는 동안
    x, y = ripe_tomato.popleft()   # 현재 토마토 지점
    for direction in range(4):  # 델타 검색으로 이동
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 박스 범위 안이고 안익은 토마토를 발견한다면
        if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0 :
            boxes[nx][ny] = boxes[x][y] + 1    # 토마토 자리에 익은 날짜 적어주기
            ripe_tomato.append((nx,ny))         # 익은 토마토 저장
max_day = 0
for i in range(n):
    for j in range(m):
        if boxes[i][j] != 0:
            if max_day < boxes[i][j]:
                max_day = boxes[i][j]
        else:
            print(-1)
            exit(0)

print(max_day-1)