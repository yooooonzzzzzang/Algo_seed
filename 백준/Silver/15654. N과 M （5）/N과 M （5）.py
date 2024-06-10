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
        if not v[i]:
            ans[x] = arr[i]
            v[i] = 1
            dfs(x+1)
            v[i] = 0
            ans[x] = 0


dfs(0)
