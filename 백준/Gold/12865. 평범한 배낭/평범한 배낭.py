n, k = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * 100010 for _ in range(n)]
answer = 0
def recur(idx, wages):
    global answer
    if wages > k:
        return -999999999999999
    if idx == n:
        return 0
    if dp[idx][wages] != -1 :
        return dp[idx][wages]
    dp[idx][wages] = max(recur(idx + 1, wages + bags[idx][0]) + bags[idx][1],
    recur(idx+1 , wages))
    return dp[idx][wages]


print(recur(0,0))
