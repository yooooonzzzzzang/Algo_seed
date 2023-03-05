from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if n == 1 and m == 1:
        return 1
    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 미로 범위 안에 있고 아직 방문 안했고 1이면:
            if 0 <= nx < n and 0<= ny <m and not visited[nx][ny] and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] =True
                queue.append((nx,ny))
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1


