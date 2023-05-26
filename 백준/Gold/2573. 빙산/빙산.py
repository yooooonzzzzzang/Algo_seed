'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''
from collections import deque
import copy

# 4방향 지나가며 빙산 녹이기
# 다음 bfs 로 개수 세기
# 개수가 2이상이면 끝
def solve(i, j):
    cnt = 0
    # 주변 빙사 있는지 확인
    if arr[i][j] ==0:
        return
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = i +di, j+dj
        if 0<=ni<N and 0<=nj<M and not arr[ni][nj]:
            cnt += 1
    tmpArr[i][j] = cnt

    # if cnt >= arr[i][j]:
    #     tmpArr[i][j] = 0
    #     # arr[i][j] = 0
    # else:
    #     # print(i,j,cnt)
    #     tmpArr[i][j] = arr[i][j] - cnt
    #     # arr[i][j]= arr[i][j] - cnt

def bfs(x2,y2,v):
    q = deque()
    q.append((x2,y2))
    v[x2][y2] = 1
    while q:
        cx,cy = q.popleft()
        for kx, ky in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = kx + cx, ky+ cy
            if not v[nx][ny] and arr[nx][ny]:
                q.append((nx,ny))
                v[nx][ny] = 1




N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
tmpArr = [[0] * M for _ in range(N)]
for year in range(1, 900000):
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                solve(i,j)  #빙산 녹이는걸 처음부터 끝까지 몇번해야할까
    for x in range(N):
        for y in range(M): # 빙산 녹은거 적용해주면 됨
            arr[x][y] = max(0, arr[x][y]-tmpArr[x][y])




    v = [[0] * M for _ in range(N)]
    cnt = 0
    for x in range(1, N-1):
        for y in range(1, M-1):
            if v[x][y] == 0 and arr[x][y] > 0:
                bfs(x,y,v)
                cnt += 1
                if cnt > 1:
                    print(year)
                    exit()

    if cnt == 0:
        print(0)
        exit()

