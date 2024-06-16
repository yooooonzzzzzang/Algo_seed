from collections import deque
arr = [input() for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]


def bfs(si,sj):
    q = deque()
    vv =  [[0]*5 for _ in range(5)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    q.append((si,sj))
    vv[si][sj] = 1
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = dx[k] + cx , dy[k] + cy
            if 0<=nx<5 and 0<=ny<5 and not vv[nx][ny] and v[nx][ny] == 1:
                q.append((nx,ny))
                vv[nx][ny] = 1
                cnt +=1
    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i,j)



def dfs(level,cnt, s_cnt):
    global ans
    if cnt >7 : # 이미 7명 넘으면 7공주 불가
        return
    if level == 25:
        if cnt == 7:
            if s_cnt >= 4:
                if check():
                    ans +=1
        return
    v[level//5][level%5] = 1
    dfs(level+1, cnt+1, s_cnt + int(arr[level//5][level%5] == 'S'))
    # 포함하지않는경우
    v[level//5][level%5] = 0
    dfs(level+1, cnt, s_cnt)


dfs(0,0,0)
print(ans)