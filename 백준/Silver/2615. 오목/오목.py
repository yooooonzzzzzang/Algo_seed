def bfs(x, y):
    target = arr[x][y]

    for k in range(4):
        cnt = 1
        nx, ny = x + dx[k], y + dy[k]

        while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == target:
            cnt += 1
            if cnt ==5:
            # 육모 체크
                if 0 <= x - dx[k] < 19 and 0 <= y-dy[k] <19 and arr[x-dx[k]][y-dy[k]]==target:
                    break
                if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and arr[nx + dx[k]][ny + dy[k]] == target:
                    break
                # 오목완성 ^^
                print(target)
                print(x+1, y+1)
                exit(0)
            nx += dx[k]
            ny += dy[k]

def w_print():
    pass
arr = [list(map(int, input().split())) for _ in range(19)]
# 1 흰, 2 검
# 검이 이기면 1, 흰이 이기면 2, 승부 ㄴ 0, 가장 왼쪽 원소의 r,c 출력

dx = [0,1,1,-1]
dy = [1,0,1,1]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            bfs(i,j)



print(0)