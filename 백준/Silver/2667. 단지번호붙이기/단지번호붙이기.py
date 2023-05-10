'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y):
    global cnt;
    cnt += 1
    maps[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx< n and 0<=ny <n and maps[nx][ny] == 1:
            dfs(nx,ny)


n = int(input())
maps = [list(map(int,input())) for _ in range(n)]
arr = []
cnt =0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            dfs(i,j)
            arr.append(cnt)
            cnt = 0

arr.sort()
print(len(arr))
for k in arr:
    print(k)