
from collections import deque
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx <n and 0<= ny < m and not maps[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for  _ in range(n)]
# 8방향
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]
answer = 0
# 상어부터 시작해야할듯 주변 8방향 +1
result = 0
q = deque()
for i in range(n):
    for j in range(m):
        # 동시에 시작 가능
        if maps[i][j] == 1:
            q.append((i,j))
bfs()
print(max(map(max, maps))-1)