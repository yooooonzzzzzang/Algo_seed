# 연결된 선이 이전 선보다 작으면 안된다! 
import sys
input = sys.stdin.readline
n = int(input())
arr =[]
dp = [1] * n

for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))