N = int(input())
arr = [[-1]*(N+2)]+[[-1]+[0]*N+[-1] for _ in range(N)]+[[-1]*(N+2)]
in_lst = [list(map(int, input().split())) for _ in range(N*N)]
sorted_lst = [[0]*5]+sorted(in_lst)

# [1] 전체를 순회하면서 빈자리에 친한친구수=>빈자리수
for lst in in_lst:
    mx = empty_mx = -1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j]>0: continue    # 빈자리가 아니면 다음위치로..
            cnt = empty_cnt = 0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj = i+di, j+dj
                if arr[ni][nj] in lst:  # 좋아하는 친구
                    cnt+=1
                if arr[ni][nj]==0:      # 빈칸인 경우
                    empty_cnt+=1
            if mx<cnt or mx==cnt and empty_mx<empty_cnt:
                mx, empty_mx = cnt, empty_cnt
                ei, ej = i, j
    arr[ei][ej] = lst[0]                # 모든위치 체크한 후 최종 자리에 번호 저장

# [2] 배치된 자리에 따른 점수 누적
tbl = [0,1,10,100,1000]
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        cnt = 0     # 네방향 친한친구수 카운트
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if arr[ni][nj] in sorted_lst[arr[i][j]]:    # 좋아하는 친구
                cnt += 1
        ans += tbl[cnt]
print(ans)