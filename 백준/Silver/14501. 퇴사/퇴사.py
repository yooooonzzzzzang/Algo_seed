
def recur(idx):
    global answer

    if idx == n:
        return 0
    if idx > n :
        return -999999999999999
    if dp[idx] != -1: # 이미 저장되었다면
        return dp[idx]
    # 상담을 받거나 안받거나 그중에서 더 많은 돈을 버는 경우를 내 dp 테이블에 저장
    dp[idx] =  max(recur(idx+arr[idx][0])+ arr[idx][1], recur(idx+1))
    return dp[idx]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n+1)
answer = 0
print(recur(0))
