def solution(n):
    answer = 1
    dp = [0,1,2,3,5,8]
    for x in range(6,n+1):
        dp.append(sum(dp[-2:]))
    answer = dp[n] %1234567
    return answer