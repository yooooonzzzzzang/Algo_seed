from collections import deque
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
n, m = map(int, input().split())
arr = list(input() for _ in range(n))

max_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            v = [[0] * (m) for _ in range(n)]
            dist = [[0] * (m) for _ in range(n)]
            q = deque()
            q.append((i,j))
            v[i][j] = 1
            while q:
                ci,cj = q.popleft()
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    ni, nj = ci + dx , cj + dy
                    if 0<=ni<n and 0<= nj<m and arr[ni][nj] == 'L' and not v[ni][nj]:
                        v[ni][nj] = 1
                        dist[ni][nj] = dist[ci][cj] + 1
                        max_cnt = max(max_cnt, dist[ni][nj])
                        q.append((ni,nj))
print(max_cnt)

