n,s = map(int, input().split())
arr = list(map(int,input().split()))

cnt = 0
def dfs(level, total):
    global cnt
    if level == n:
        if total == s:
            cnt += 1
        return

    dfs(level+1, total + arr[level])
    dfs(level+1, total)
dfs(0,0)
if s == 0:
    print(cnt-1)
else:
    print(cnt)

