from collections import deque


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
def bfs(x,y,h):
    v[x][y] = 1
    q = deque()
    q.append((x,y))

    while q:
        cx, cy= q.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and not v[nx][ny] and arr[nx][ny] > h:
                q.append((nx,ny))
                v[nx][ny] = 1


def solve(h):
    cnt =0
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j]>h:
                bfs(i,j,h)
                cnt +=1
    return cnt

for h in range(100): # 높이 0~99 까지 물 높이
    v = [[0] * (N) for _ in range(N)]
    max_cnt = max(max_cnt, solve(h))
print(max_cnt)
