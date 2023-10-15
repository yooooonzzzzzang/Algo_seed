n, m = map(int,input().split())
arr =sorted(map(int, input().split()))
tmp = []
def recur(start):
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(start, n):
        if arr[i] not in tmp:
            tmp.append(arr[i])
            recur(i+1)
            tmp.pop()
#
recur(0)