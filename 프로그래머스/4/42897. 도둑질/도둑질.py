def solution(money):
    n = len(money)
    # 첫 번째 집을 턴 경우, 마지막 집은 털 수 없다
    dp1 = [0] + money[:-1]
    # 두 번째 집을 턴 경우, 처음집 x
    dp2 = [0] + money[1:]
    for i in range(2,n):
        dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
    for i in range(2,n):
        dp2[i] = max(dp2[i] + dp2[i-2], dp2[i-1])
    return max(dp1[-1], dp2[-1])