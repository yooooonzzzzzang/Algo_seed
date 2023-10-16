c, r  = map(int, input().split())
k = int(input())



if r * c < k:
    print(0)
else:
    # 아래 오른 위 왼
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 주변을 1로 둘러싸면 : 범위 체크 필요없음
    arr = [[1]*(c+2)] + [[1] + [0]*c + [1] for _ in range(r)] + [[1]*(c+2)]

    cx, cy, dr = 1,1,0
    for n in range(1, k):
        arr[cx][cy]  = n
        nx, ny = cx + dx[dr], cy + dy[dr]
        if arr[nx][ny] == 0: # 빈자리, 이동가능
            cx, cy = nx, ny
        else:                # 범위 밖이나 이미 자리있음 -> 다른 방향
            dr = (dr + 1) % 4
            cx , cy = cx + dx[dr] , cy + dy[dr]

    print(cy, cx)