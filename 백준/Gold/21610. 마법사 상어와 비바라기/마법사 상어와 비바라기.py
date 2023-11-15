# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0,0, -1, -1, -1, 0, 1, 1, 1]
dy = [0,-1, -1, 0, 1, 1, 1, 0, -1]
n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
clist = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    d, s = map(int, input().split())
    # 구름 이동 , 물의 양 1 증가 , 구름 사라짐
    clist2 = []
    for ci, cj in clist:
        # 배열 양끝을 이을 수 있음
        ni, nj = (ci+dx[d]*s+n)%n , (cj+dy[d]*s+n)%n
        arr[ni][nj] += 1
        clist2.append((ni,nj))
    # 대각선 물복사
    # 시간 단촉 용
    v = [[0] * n  for _ in range(n)]
    d_dx = [-1, -1, 1, 1]
    d_dy = [-1, 1, -1, 1]
    for ci, cj in clist2:
        for k in range(4):
            v[ci][cj] = 1 # 시간 단축용 구름위치 룩업테이블 표시
            d_ni, d_nj = ci + d_dx[k], cj + d_dy[k]
            if 0<= d_ni < n and 0 <= d_nj < n and arr[d_ni][d_nj] > 0:
                arr[ci][cj] += 1
        # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
        # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    clist =[]
    for i in range(n):
        for j in range(n):
            # if arr[i][j] >= 2 and (i,j) not in clist2:
            if arr[i][j] >= 2 and v[i][j] == 0 :
                arr[i][j] -=2
                clist.append((i,j))

ans = 0
for list in arr:
    ans += sum(list)

print(ans)