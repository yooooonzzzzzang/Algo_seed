n,m = map(int, input().split())
arr = []
def recur():
    if len(arr) == m:
        print(*arr)
        return 
    for i in range(1, n+1):
        arr.append(i)
        recur()
        arr.pop()
recur()