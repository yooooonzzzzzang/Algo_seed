import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, d = map(int, input().split())
r = r-1
c = c-1
temp = copy.deepcopy(grid)
# Write your code here!
def rotate(d):
    global r, c 
    if d == 0 :
        dxs, dys = [-1,-1,1,1],[1,-1,-1,1]
        dirLen = [m1,m2,m3,m4]
    else:
        dxs, dys = [-1,-1,1,1],[-1,1,1,-1]
        dirLen = [m4,m3,m2,m1]
    for i in range(4):
        for _ in range(dirLen[i]):
            nx, ny = r + dxs[i], c + dys[i]
            temp[nx][ny] = grid[r][c]
            r,c = nx,ny 
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]
    

rotate(d)
for i in grid:
    print(*i)