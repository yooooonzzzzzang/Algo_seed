import heapq
t = 1
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def dijkstra(x,y):
    INF = 1e9
    distance = [[INF] * (n)  for _ in range(n)]
    heap = [(arr[x][y],x,y)]
    while heap:
        min_dist, min_x,min_y = heapq.heappop(heap)
        if min_dist > distance[min_x][min_y]:
            continue
        for k in range(4):
            nx, ny = dx[k]+min_x, dy[k]+min_y

            if 0<=nx<n and 0<=ny<n:
                new_dist = arr[nx][ny] + min_dist
                if distance[nx][ny] > new_dist:
                    distance[nx][ny] = new_dist
                    heapq.heappush(heap,(new_dist, nx,ny))
    return distance[n-1][n-1]
while True:
    n = int(input())

    if n==0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = dijkstra(0,0)
    print("Problem %d: %d" %(t, ans))
    t +=1