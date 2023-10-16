n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
def recur(idx, total):
    global answer

    if idx > n-1:
        if idx > n: return
        answer = max(answer, total)
        return
    recur(idx+arr[idx][0], total+arr[idx][1])
    recur(idx+1, total)

recur(0,0)
print(answer)