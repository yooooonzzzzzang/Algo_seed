n = int(input())
# 피보나치
dp = [0 for _ in range(1010)]
dp[1] = 1
dp[2] = 2
if n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i-2] +dp[i-1]

print(dp[n] % 10007)