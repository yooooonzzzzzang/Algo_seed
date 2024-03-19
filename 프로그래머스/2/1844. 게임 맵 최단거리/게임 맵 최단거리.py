from collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    v[0][0] =1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x + dx[k] , y + dy[k]
            if 0<=nx<n and 0<= ny <m and not v[nx][ny] and maps[nx][ny] == 1:
                q.append((nx,ny))
                v[nx][ny] = v[x][y] + 1
    
        
    return v[n-1][m-1] if v[n-1][m-1] else -1