from collections import deque
def bfs(s, cnt):
    q = deque()
    q.append((s, cnt))
    v[s] = 1
    while q:
        s, cnt = q.popleft()
        if s == g:
            return cnt
        for i in (s + u, s - d):
            if 1<=i<=f and not v[i]:
                q.append((i, cnt+1))
                v[i] = 1
    return "use the stairs"
f,s,g,u,d = map(int, input().split())
# 총 f , 현재 s , 목표 g,
v = [0] *(1000000+1)

print(bfs(s, 0))
