n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]
# 1 8 2 3 9
for i in range(1, n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))