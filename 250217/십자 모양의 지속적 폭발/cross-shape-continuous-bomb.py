n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]



def init(affect, x,y):
    #터진다
    for i in range(n):
        for j in range(n):
            if abs(i-x) + abs(j-y)  <= affect-1  and (i == x or j==y ):
                grid[i][j] = 0
    #내려간다
    newGrid = [[0] * n for _ in range(n)]
    for j in range(n):
        # 
        newi = n-1
        for i in range(n-1,-1,-1):
            if grid[i][j] != 0 :
                newGrid[newi][j] = grid[i][j]
                newi -=1
    for i in range(n):
        for j in range(n):
            grid[i][j] = newGrid[i][j]

# Write your code here!
for i in range(m):
    for j in range(n):
        if grid[j][commands[i]-1] > 0:
            # 터진다.
            init(grid[j][commands[i]-1], j,commands[i]-1)
            break
        else:
            continue
for i in grid:
    print(*i)