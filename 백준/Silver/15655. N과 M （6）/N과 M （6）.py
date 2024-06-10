n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

ans = [0] * m
v = [0] * n

def dfs(x, start):
    if x == m:
        print(*ans)
        return
    for i in range(start, n):
        if not v[i]:
            ans[x] = arr[i]
            v[i] = 1
            dfs(x+1, i)
            v[i] = 0
            ans[x] = 0


dfs(0,0)
