from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    def makeLine(xy):
        for i in range(xy[0],xy[2]+1):
            for j in range(xy[1],xy[3]+1):
                if (i == xy[0] or i == xy[2] or j == xy[1] or j == xy[3] ) and graph[i][j] != 2:
                    graph[i][j] = 1
                else:
                    graph[i][j] = 2
    
    def bfs(cx, cy, ix, iy):
        q = deque()
        q.append((cx, cy, 0))
        v[cx][cy] = 1
        
        while q:
            x, y,cnt = q.popleft()
            #  answer
            if x==ix and y==iy:
                return cnt//2
            
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<102 and 0<=ny<102 and graph[nx][ny]==1 and not v[nx][ny]:
                    q.append((nx,ny, cnt+1))
                    v[nx][ny] = 1
        return 0
    
    
    answer = 0
    # 50 * 2 
    graph = [[0] * 102 for _ in range(102)]
    v = [[0] * 102 for _ in range(102)]
    
    for rec in rectangle:
        for j in range(len(rec)):
            rec[j] *= 2
        makeLine(rec)
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2)
    return answer