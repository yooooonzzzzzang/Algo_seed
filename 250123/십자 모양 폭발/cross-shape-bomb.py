n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Write your code here!
# 폭판 터지기  -> 0 으로 변경 
def bomb(x,y):
    bombSize = grid[x][y] - 1
    grid[x][y] = 0
    for dx, dy in zip((-1,1,0,0),(0,0,-1,1)):
        cx, cy = x,y
        for _ in range(bombSize):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and  0<=ny<n:
                grid[nx][ny] = 0
                cx,cy = nx,ny
# 내려오기 -> 0 이면 pass 
def down():
    temp = [[0] *n for _ in range(n)]
    for j in range(n):
        idx = n-1
        for i in range(n-1,-1,-1):
            if grid[i][j] != 0:
                temp[idx][j] = grid[i][j]
                idx -= 1
    return temp

bomb(r-1,c-1)
new = down()
for i in new:
    print(*i)