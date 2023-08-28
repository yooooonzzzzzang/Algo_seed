'''
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1
'''

# 3개의 꽃(5칸) 이 최소 비용으로 필 때 그 가격
N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
answer = 999999999
# 현위치, 상, 하, 좌, 우
dir = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
v = [[False] * N for _ in range(N)]

'''
 조건: 1) 꽃잎이 완성되는지(5개)
      2) 꽃이 3개인지
      3) 최소비용인지 
      조건을 어디에 배치해둘것인지  
'''

def check(x,y):
    global N
    for dy, dx in dir:
        nx, ny = dx+x, dy+y
        if not(0<= nx<N and 0<=ny<N) or v[nx][ny]:
            return False
    return True
def calculate(x,y):
    global N
    result = 0
    for dx,dy in dir:
        nx, ny = dx+x, dy+y
        result += maps[nx][ny]
    return result

def dfs(x, cost, cnt):
    global answer
    # 2) 꽃이 세개인지
    if cnt == 3:
        # 3) 최소비용인지
        answer = min(answer, cost)
        return
    for i in range(x, N):
        for j in range(1, N):
            # 1) 꽃잎 완성 되는지
            if check(i,j):
                v[i][j] = True
                for dx, dy in dir:
                    v[i + dx][j + dy] = True
                dfs(i, cost + calculate(i, j), cnt + 1)
                v[i][j] = False
                for dx, dy in dir:
                    v[i + dx][j + dy] = False







dfs(1,0,0)
print(answer)
