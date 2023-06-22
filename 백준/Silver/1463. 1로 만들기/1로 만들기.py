n = int(input())
dp = [0,0,1,1]
for x in range(4,n+1):
    dp.append(dp[x-1]+1)
    if x % 2 ==0:
        dp[x] = min(dp[x//2]+1, dp[x])
    if x % 3 == 0:
        dp[x] = min(dp[x//3]+1, dp[x])

print(dp[n])