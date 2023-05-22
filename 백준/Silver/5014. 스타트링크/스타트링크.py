
'''
F: 총 건물의 층
S: 현재 층
G: 목표 층
U: 위로 u 만큼 간다
D: 아래로 d 만큼 간다
'''
from collections import deque
def bfs(s):
    global cnt
    cnt = 0
    visited = [0] *(F+1)
    q = deque()
    visited[s] = 1
    q.append((s, cnt))
    while q:
        k, newcnt = q.popleft()
        if k == G:
            return newcnt
        # 조건
        if F >= k + U and not visited[k+U]:
            visited[k+U] = 1
            q.append((k+U, newcnt+1))

        if k - D > 0 and not visited[k-D]:
            q.append((k-D, newcnt+1))
            visited[k-D] = 1

    return "use the stairs"




F, S, G, U, D = map(int,input().split())
cnt = 0
print(bfs(S))