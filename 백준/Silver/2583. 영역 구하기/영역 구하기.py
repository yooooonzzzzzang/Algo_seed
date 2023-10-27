'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
import sys
sys.setrecursionlimit(1000000)

m,n,k = map(int,input().split())
arr = [[0] * n for _ in range(m)]
v = [[0] * n for _ in range(m)]
def dfs(x,y):
    global cnt
    cnt+=1
    v[x][y] = 1
    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx, ny = x+dx, y+dy
        if 0<=nx<m and 0<=ny<n and arr[nx][ny] == 0 and not v[nx][ny] :
            dfs(nx,ny)
# 뒤집어진 arr
for i in range(k):
    y1, x1, y2,x2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

    # dfs 로 공간
ans = []
for i in range(m):
    for j in range(n):
        cnt = 0
        if arr[i][j] == 0 and not v[i][j]:
            dfs(i,j)
            ans.append(cnt)
print(len(ans))
print(*sorted(ans))
