n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(lambda x:x-1, map(int, input().split()))) for _ in range(n)]
r, c = map(int, input().split())
r,c = r-1,c-1
# Please write your code here.
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

ans = 0
def recur(dir_v, x, y, cnt):
    global ans

        # 방향만큼 얼만큼 갈수 있는지 
    for i in range(1,n+1):
        nx = x + (dxs[dir_v] *i)
        ny = y + (dys[dir_v] *i)
        if 0 <= nx <n and 0<= ny <n and num[nx][ny] > num[x][y]:
            recur(move_dir[nx][ny],nx, ny, cnt+1)
        else:
            ans = max(ans,cnt)
            return 
recur(move_dir[r][c],r,c,1) 
print(ans if n != 1 else 0)