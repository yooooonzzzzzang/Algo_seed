n = int(input())
arr = []
for i in range(n):
    arr.append((list(map(int, input().split()))))
arr.sort(key=lambda x: x[0])
last_length = arr[-1][0]

prefix = [0] * (last_length+ 1)
# 높이가 max 인 x  ==> index
max_value = max(arr, key=lambda x: x[1])
max_index  = arr.index(max(arr, key=lambda x: x[1]))
for i in range(max_index):
    prefix[i+1] = max(arr[i][1], prefix[i])

for i in range(n-1, max_index,-1):
    prefix[i] = max(arr[i][1], prefix[i+1])

# 0 ~6
ans = 0
for i in range(n-1):
    ans += (prefix[i+1] * (arr[i+1][0] -arr[i][0]))
ans += max_value[1]
print(ans)