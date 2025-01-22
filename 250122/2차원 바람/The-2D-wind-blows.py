n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

def rotate(x1,y1,x2,y2):
    tmp = a[x1][y1]
    for i in range(x1, x2):
        a[i][y1] = a[i+1][y1]
    for i in range(y1, y2):
        a[x2][i] = a[x2][i+1]
    for i in range(x2,x1,-1):
        a[i][y2] = a[i-1][y2]
    for i in range(y2,y1,-1):
        a[x1][i] = a[x1][i-1]
    a[x1][y1+1] = tmp


def calculate(x1,y1,x2,y2):
    # copy a -> new_a 
    new_a = [[0] * m for _ in range(n)]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            tmp = a[i][j]
            cnt = 1
            for dx, dy  in ((-1,0),(0,-1),(1,0),(0,1)):
                ni, nj = i+dx, j+dy
                if 0<=ni<n and 0<=nj<m:
                    tmp += a[ni][nj]
                    cnt += 1
            tmp /= cnt
            tmp = int(tmp)
            new_a[i][j] = tmp
            # a[i][j]
    for i in range(x1,x2+1):
        for j in range(y1, y2+1):
            a[i][j] = new_a[i][j]

# 1. 경계면 회전
for i in range(q):
    r1,c1,r2,c2 = map(lambda x: x-1, winds[i])
    rotate(r1,c1,r2,c2)
    calculate(r1,c1,r2,c2)

for i in a:
    print(*i)
# 2. 인접원소 평균값 변경



