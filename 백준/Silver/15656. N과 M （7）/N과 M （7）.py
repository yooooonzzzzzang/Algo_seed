n,m = map(int, input().split())
arr = sorted(map(int, input().split()))
tmp = []
def recur():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(n):
        tmp.append(arr[i])
        recur()
        tmp.pop()

recur()