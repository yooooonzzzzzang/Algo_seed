'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
from collections import deque
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    cnt = 0
    while queue:
        k = queue.popleft()
        for next_v in com[k]:
            if not visited[next_v]:
                visited[next_v] = 1
                queue.append(next_v)
                cnt += 1
    return cnt
n = int(input())
m = int(input())
com =[[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    v1, v2 = map(int, input().split())
    com[v1].append(v2)
    com[v2].append(v1)
print(bfs(1))