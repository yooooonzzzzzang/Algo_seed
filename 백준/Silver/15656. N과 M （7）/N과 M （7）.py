n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

ans = [0] * m
v = [0] * n

def dfs(x):
    if x == m:
        print(*ans)
        return
    for i in range(n):
        ans[x] = arr[i]
        dfs(x+1)
        # ans[x] = 0


dfs(0)
