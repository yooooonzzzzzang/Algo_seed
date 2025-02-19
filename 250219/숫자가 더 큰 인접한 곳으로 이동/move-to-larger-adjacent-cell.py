n,r,c = map(int,input().split())
r,c = r-1, c-1

arr = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [-1,1,0,0],[0,0,-1,1]


x,y = r,c
ans =[arr[x][y]]
while True:
    isMoved = False

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<= ny<n and arr[nx][ny] > arr[x][y]:
            isMoved = True
            x,y = nx, ny
            ans.append(arr[x][y])
            break
     
    if not isMoved:
        break
print(*ans)