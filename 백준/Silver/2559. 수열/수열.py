n,k = map(int, input().split())
arr = list(map(int,input().split()))
answer = []
pre = 0
prefix_sum = [0]
for i in range(n):
    pre += arr[i]
    prefix_sum.append(pre)
for i in range(n-k+1):
    part_sum = prefix_sum[i+k] - prefix_sum[i]
    answer.append(part_sum)
print(max(answer))
