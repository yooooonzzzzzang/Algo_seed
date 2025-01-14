n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n-3+1):
    for j in range(n-3+1):
        tmp = 0
        for k in range(i,i+3):
            for l in range(j,j+3):
                if grid[k][l] == 1:
                    tmp+=1
        ans = max(ans, tmp)

print(ans)