n, m = map(int, input().split())
arr = []
def recur(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n+1):
        arr.append(i)
        recur(i)
        arr.pop()

recur(1)