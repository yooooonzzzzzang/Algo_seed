
def dfs(level, start):
    global cnt
    if level == 6:
        print(*tmp)
        return 
    for i in range(start, n):
        tmp[level] = arr[i]
        dfs(level+1, i+1)
        tmp[level] = 0

while True:
    inputs = list(map(int, input().split()))
    n = inputs[0]
    arr = inputs[1:]
    if len(inputs) == 1 and inputs[0] == 0:
        break
    tmp = [0] * 6
    cnt = 0
    dfs(0,0)
    print(" ")
