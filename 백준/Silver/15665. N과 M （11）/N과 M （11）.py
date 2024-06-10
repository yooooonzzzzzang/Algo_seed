n, m = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()
ans = [0]*m

def dfs(level):
    if level == m:
        print(*ans)
        return
    else:
        check = 0
        for i in range(n):
            if check != arr[i]:
                check = arr[i]
                ans[level] = arr[i]
                dfs(level+1)
dfs(0)