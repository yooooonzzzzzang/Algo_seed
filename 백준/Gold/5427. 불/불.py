from collections import deque
def bfs():
    time  = 0
    global ans

    while q:
        time += 1
        # 불 1초동안 확장
        for _ in range(len(fires)):
            x, y = fires.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (arr[nx][ny] == "." or arr[nx][ny] =="@") :
                    arr[nx][ny] = "*"
                    fires.append((nx, ny))

        # 사람 이동
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == ".":
                        arr[nx][ny] = "@"
                        q.append((nx, ny))
                # 범위 탈출조건
                else:
                    ans = time
                    return



for t in range(int(input())):
    m,n = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    v = [[-1] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    ans ="IMPOSSIBLE"
    fires = deque()
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                fires.append((i,j))
            elif arr[i][j] == '@':
                q.append((i,j))
    bfs()
    print(ans)
