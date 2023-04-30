def bfs(s,e):
    queue =[]
    visited = [0] *(n+1)

    queue.append(s)
    visited[s] = 1

    while queue:
        c = queue.pop(0)
        if c == e:
            return visited[e] -1
        #  c 와 연결된 번호인 경우 미방문이면 방문
        for next_v in family[c]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] += visited[c] + 1
    return -1
n = int(input())
s, e = map(int, input().split())
cnt = 1
m = int(input())
family = [[] for _ in range( n+1)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    family[m2].append(m1)
    family[m1].append(m2)
print(bfs(s,e))