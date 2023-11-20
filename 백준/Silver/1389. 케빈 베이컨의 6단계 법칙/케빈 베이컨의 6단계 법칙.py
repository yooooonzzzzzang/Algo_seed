from collections import deque
def bfs(i):
    v = [0] * (n + 1)
    distance_num = [0] * (n + 1)
    q = deque()
    q.append(i)
    v[i] = 1
    while q:
        num = q.popleft()
        for next in arr[num]:
            if not v[next]:
                v[next] = 1
                distance_num[next] = distance_num[num]+1
                q.append(next)
    return sum(distance_num)

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)