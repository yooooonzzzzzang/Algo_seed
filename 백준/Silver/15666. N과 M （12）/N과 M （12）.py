n, m = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()
ans = [0]*m

def dfs(level, start):
    if level == m:
        print(*ans)
        return
    else:
        check = 0
        for i in range(start, n):
            if check != arr[i] :
                check = arr[i]
                ans[level] = arr[i]
                dfs(level+1, i)
dfs(0,0)