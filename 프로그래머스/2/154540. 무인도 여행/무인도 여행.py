from collections import deque
def solution(maps):
    def bfs(x,y):
        v[x][y] = True
        total = int(maps[i][j])
        q = deque()
        q.append((x,y))
        while q:
            x, y = q.popleft()
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx, ny = x + dx , y+dy
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] != 'X' and v[nx][ny] != 1:
                    v[nx][ny] = 1
                    q.append((nx,ny))
                    total += int(maps[nx][ny])
        return total
    answer = []
    v = [[0] * len(maps[1]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and v[i][j] == 0:
                answer.append(bfs(i,j))
    
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]