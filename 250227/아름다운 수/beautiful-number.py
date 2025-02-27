def count_ways(n):
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1  # 0을 만드는 방법은 아무것도 안 더하는 한 가지 경우
    for i in range(1, n + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 2] if i - 2 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0
        dp[i] += dp[i - 4] if i - 4 >= 0 else 0
    return dp[n]

n = int(input()) # 예제 값
print(count_ways(n))  # 출력: 274
