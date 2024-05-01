import heapq
def djikstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue
        for nxt_node, nxt_dist in graph[node]:
            new_dist = dist + nxt_dist
            if new_dist < distance[nxt_node]:
                distance[nxt_node] = new_dist
                heapq.heappush(heap,(new_dist, nxt_node))
    return distance
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 1e9

for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))

# 출발
depart = djikstra(x)
ans = []
# 돌아오는 길
for i in range(1, n+1):
    tmp = djikstra(i)
    ans.append(depart[i] + tmp[x])
print(max(ans))