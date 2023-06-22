for t in range(int(input())):
    n = int(input())
    dp = [0,1,2,4,7]
    
    for i in range(5, n+1):
        dp.append(sum(dp[-3:]))


    print(dp[n])