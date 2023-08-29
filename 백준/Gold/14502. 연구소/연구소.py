'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
import sys
sys.setrecursionlimit(100000)
from itertools import combinations
import copy
N,M = map(int,input().split())
maps = [input().split() for _ in range(N)]
dx =[-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<M and maps2[nx][ny] == '0':
            maps2[nx][ny] = '2'
            dfs(nx,ny)



arr = []
# 0 인 좌표 구하기
for i in range(N):
    for j in range(M):
        if maps[i][j] == '0':
            arr.append((i,j))

safe_area = 0
for combination in list(combinations(arr,3)):
    # 2차 연구소
    # maps2 = copy.deepcopy(maps)
    maps2 = [[0] *M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            maps2[i][j] = maps[i][j]
    # 3개 벽 추가
    for comb in combination:
        r,c = comb
        maps2[r][c] = '1'
    # 감염
    for i in range(N):
        for j in range(M):
            if maps2[i][j] == '2':
                dfs(i,j)
    # 안전영억 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps2[i][j] == '0':
                cnt += 1
    safe_area = max(safe_area, cnt)
print(safe_area)
# 벽 3군데 세우기

# dfs 돌기
# 0 cnt