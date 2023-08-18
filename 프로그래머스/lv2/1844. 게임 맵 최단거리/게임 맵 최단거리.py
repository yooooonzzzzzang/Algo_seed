
from collections import deque
def solution(maps):
    answer = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    v = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    q = deque()
    v[0][0] = 1
    q.append((0,0))
    while q:
        x,y = q.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            return maps[len(maps)-1][len(maps[0])-1]
        for dir in range(4):
            nx, ny = dx[dir] + x , dy[dir] + y 
            if 0<= nx <len(maps) and 0<= ny <len(maps[0]) and not v[nx][ny] and maps[nx][ny] ==1:
                v[nx][ny] = True
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
    return -1