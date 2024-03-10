def solution(N, number):
    answer = 0
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    print(dp[5])
    print(dp)
    
    for i in range(8):
        for j in range(i):
            for arg1 in dp[j]:
                for arg2 in dp[i-j-1]:
                    dp[i].add(arg1+arg2)
                    dp[i].add(arg1-arg2)
                    dp[i].add(arg1*arg2)
                    if arg2 != 0:
                        dp[i].add(arg1//arg2)
        if number in dp[i]:
            return i+1

    return -1