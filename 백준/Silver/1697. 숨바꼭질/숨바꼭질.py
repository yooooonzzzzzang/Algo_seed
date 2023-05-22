from collections import deque

def bfs(N,K):
    v = [0] * (100000+1)
    second = 0
    q = deque()
    q.append((N, second))
    v[N] = 1
    while q:
        cur_n, cur_second = q.popleft()
        if cur_n == K:
            return cur_second
        for position in (cur_n-1, cur_n+1, cur_n*2):
            if 0<= position<= 100000 and not v[position]:
                v[position] = 1
                q.append((position, cur_second+1))



N,K = map(int,input().split())
print(bfs(N,K))