ans = 0

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]



def init(affect, x,y):
    copygrid =[[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copygrid[i][j] = grid[i][j]
    #터진다
    for i in range(n):
        for j in range(n):
            if abs(i-x) + abs(j-y)  <= affect-1  and (i == x or j==y ):
                copygrid[i][j] = 0
    #내려간다
    newGrid = [[0] * n for _ in range(n)]
    for j in range(n):
        # 
        newi = n-1
        for i in range(n-1,-1,-1):
            if copygrid[i][j] != 0 :
                newGrid[newi][j] = copygrid[i][j]
                newi -=1
   
    cnt = 0

   
    # 인접숫자확인 
    for i in range(n):
        for j in range(n):
            for dx, dy in ((1,0),(0,1)):
                if 0<=i+dx<n and 0<= j+dy<n:
                    if newGrid[i][j] == newGrid[i+dx][j+dy] and newGrid[i][j] != 0:
                        cnt +=1
    return cnt

# Write your code here!
for i in range(n):
    for j in range(n):
            # 터진다.
            ans = max(init(grid[i][j],i,j), ans)

print(ans)