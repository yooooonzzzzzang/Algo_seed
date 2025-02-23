n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
minI =  n-1
did = False
for i in range(n):
    for j in range(k-1, k+m-1):
        if arr[i][j] != 0:
            minI = i-1
            did = True
            break
    if did :
        break
for j in range(k-1,k+m-1):
    arr[minI][j] = 1

for col in arr:
    print(*col)