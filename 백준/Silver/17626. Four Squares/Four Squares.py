n = int(input())
dp = [0,1,2,3,1,2,3,4,2,1]
if n>=10:
    for i in range(10, n+1):
        min_v = 4
        for j in range(1,int(i**0.5)+1):
            min_v = min(min_v, dp[i-j**2])
        dp.append(min_v+1)



print(dp[n])
