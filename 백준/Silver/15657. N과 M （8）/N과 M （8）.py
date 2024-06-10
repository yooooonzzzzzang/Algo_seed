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
        ans[x] = arr[i]
        dfs(x+1, i)
        # ans[x] = 0


dfs(0,0)
