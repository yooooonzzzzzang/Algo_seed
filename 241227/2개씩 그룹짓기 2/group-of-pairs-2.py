import sys
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

min_diff = sys.maxsize 
for i in range(n):
    min_diff = min(min_diff, arr[n + i] - arr[i])

print(min_diff)