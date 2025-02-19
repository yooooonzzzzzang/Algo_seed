n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
minI = 100000
for j in range(k-1, k+m-1):
    for i in range(n-1,-1,-1):
        if arr[i][j] == 0:
            if minI > i:
                minI = i
            break
for j in range(k-1,k+m-1):
    arr[minI][j] = 1

for col in arr:
    print(*col)