n, x = map(int,input().split())
visit = list(map(int, input().split()))
# print(visit)
if sum(visit) == 0:
    print("SAD")
    exit(0)
dp = [0] * (n+1)
for i in range(len(visit)):
    dp[i+1] = dp[i] + visit[i]
max_v = 0
for i in range(n-x+1):
    if max_v == dp[i+x] - dp[i]:
        cnt += 1
    elif max_v < dp[i+x] - dp[i]:
        cnt = 1
        max_v = dp[i+x] - dp[i]

print(max_v)
print(cnt)
# x일 동안 가장 많이 들어온 방문자 수 sum(range(x)) 0> sad
# sad 아니면 18일이면 그게 몇개 있는지