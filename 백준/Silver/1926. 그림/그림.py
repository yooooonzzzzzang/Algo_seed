from collections import deque
def bfs(i,j):
    global max_cnt
    v[i][j] = 1
    q = deque()
    q.append((i,j))
    total = 1
    while q:
        x,y = q.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = x+dx , y+dy
            if 0<=nx<n and 0<=ny<m and not v[nx][ny] and arr[nx][ny]:
                q.append((nx,ny))
                v[nx][ny] = 1
                total += 1
    max_cnt = max(max_cnt, total)
                

ans = 0
max_cnt = 0
n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
cnt  =0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not v[i][j]:
            bfs(i,j)
            cnt += 1

print(cnt)
print(max_cnt)