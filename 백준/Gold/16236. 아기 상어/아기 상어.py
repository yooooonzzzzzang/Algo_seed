from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark_size = 2
shark_eat = 0
time = 0

# 상어위치 저장
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            x, y = i,j

# 가장 가까운 물고기 pick
def bfs(x, y, shark_size):
    d = [[0] * n for _ in range(n)]
    v = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x,y))
    v[x][y] = 1
    tmp = []

    while q:
        cur_x, cur_y = q.popleft()
        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                if maps[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    v[nx][ny] = 1
                    d[nx][ny] = d[cur_x][cur_y] + 1
                    # 상어가 현재 잡을 수 있는 물고기
                    if maps[nx][ny] < shark_size and maps[nx][ny] != 0:
                        tmp.append((nx, ny, d[nx][ny]))
    #d가 가장 작은,  x가 가장 작은, y 가 가장 작은 순 ==
    return sorted(tmp, key=lambda x : (-x[2], -x[0], -x[1]))


while True:
    fishes = bfs(x,y,shark_size)
    # 먹을 물고기가 없다면 break
    if len(fishes) == 0:
        break

    nx, ny, distance = fishes.pop()

    time += distance
    maps[x][y], maps[nx][ny] = 0, 0
    x,y = nx, ny

    shark_eat += 1

    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

print(time)