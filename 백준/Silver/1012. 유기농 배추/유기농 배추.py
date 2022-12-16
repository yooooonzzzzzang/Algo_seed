import sys

sys.setrecursionlimit(1000000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and fields[nx][ny]:
            dfs(nx, ny)


for tc in range(int(input())):
    m, n, k = map(int, input().split())     # m:가로 n:세로 k:심은 배추 개수
    fields = [[0] * m for _ in range(n)]
                                            # 밭에 배추 심기
    for _ in range(k):
        c, r = map(int, input().split())
        fields[r][c] = 1

    visited = [[False]* m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and fields[i][j]:           # 방문하지 않고 배추가 심어져 있으면
                dfs(i, j)
                cnt += 1
    print(cnt)