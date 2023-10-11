n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
ans = []
for i in range(n-k+1):
    ans.append(prefix[i+k] - prefix[i])
print(max(ans))