n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# Write your code here!
for i in range(n):
    tmp = 1
    flag = False
    for j in range(1, n):
        if grid[i][j] != grid[i][j-1]:
            if tmp >= m:
                flag = True
                break
            flag= False
            tmp = 1
        else:
            tmp += 1
            flag = True
    if flag == True and tmp >= m:
        ans += 1

for j in range(n):
    tmp = 1
    flag = False
    for i in range(1, n):
        if grid[i][j] != grid[i-1][j]:
            if tmp >= m:
                flag = True
                break
            flag= False
            tmp = 1
        else:
            tmp += 1
            flag = True
    if flag == True and tmp >= m:
        ans += 1
print(2) if n == 1 and m == 1 else print(ans)