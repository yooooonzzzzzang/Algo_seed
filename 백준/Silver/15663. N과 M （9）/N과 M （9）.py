n, m = map(int, input().split())
arr= list(map(int, input().split()))
arr.sort()
ans = [0]*m
v = [0] * n

def dfs(level):
    check = 0
    if level == m:
        print(*ans)
        return
    else:

        for i in range(n):
            if v[i] == 0 and check != arr[i] :
                check = arr[i]
                ans[level] = arr[i]
                v[i] = 1
                dfs(level+1)
                v[i] = 0
dfs(0)