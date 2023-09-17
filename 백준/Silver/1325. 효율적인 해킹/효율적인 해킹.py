from collections import deque
from sys import stdin
def bfs(n):
    q = deque()
    q.append(n)
    cnt = 1
    v = [0] * (N+1)
    v[n] = True
    while q:
        x = q.popleft()
        for nx in node[x]:
            if not v[nx]:
                v[nx] = True
                q.append(nx)
                cnt += 1
    return cnt

N, M = map(int,input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    num1, num2 = map(int,stdin.readline().split())
    node[num2].append(num1)

answer = []

for i in range(1, N+1):
    answer.append(bfs(i))

max_cnt = max(answer)
for i in range(len(answer)):
    if max_cnt == answer[i]:
        print(i+1, end=' ')