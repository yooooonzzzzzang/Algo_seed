
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True  # 시작 좌표 방문 처리
    queue = [(x, y)]  # 시작 좌표를 넣고 큐를 초기화
    global result
    while queue:    # 큐에 값이 있는동안
        x, y = queue.pop(0)  # 현재 방문 지점
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 지도의 범위 안에 있고 & 아직 방문하지 않았으며 & 집이 있다면
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    result = 1
                    return
                visited[nx][ny] = True  # 방문처리
                queue.append((nx, ny))  # 방문한 좌표 큐에 넣음



for t in range(1, 10 + 1):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    result = 0
    start = (1, 1)
    end = ()
    visited = [[False] * 16 for _ in range(16)]


    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                bfs(i, j)

    print(f'#{t} {result}')